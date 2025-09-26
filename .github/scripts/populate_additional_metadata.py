import ast
import base64
import concurrent.futures
import functools
import os
import queue
import sys
import threading
import traceback
from datetime import datetime
from pathlib import Path

import requests
import ruamel.yaml

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)

PLUGINSTATS_7D_URL = "https://data.octoprint.org/export/plugin_stats_7d.json"
PLUGINSTATS_30D_URL = "https://data.octoprint.org/export/plugin_stats_30d.json"

BATCH_SIZE = 10

GITHUB_PREFIX = "https://github.com/"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
GITHUB_GRAPHQL_QUERY = """repository(owner: \"{{user}}\", name: \"{{repo}}\") {
  openIssues: issues(first:1, states: OPEN) {
    totalCount
  },
  closedIssues: issues(first:1, states: CLOSED) {
    totalCount
  },
  lastRelease: releases(first:1, orderBy:{ direction:DESC, field:CREATED_AT }){
    totalCount,
    nodes {
      name,
      publishedAt,
      url,
      tagName,
      isPrerelease
    }
  },
  lastPush: defaultBranchRef {
    target {
      ... on Commit {
        history(first: 1){
          edges{
            node {
              committedDate
            }
          }
        }
      }
    }
  },
  watchers(first:1){
    totalCount
  },
  stargazers(first:1){
    totalCount
  }
}
"""

GITHUB_REST_URL = "https://api.github.com"

file_counter = 0
github_graphql_counter = 0
github_rest_counter = 0

def to_date(date_str):
    return datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime(
        "%Y-%m-%d %H:%M:%S %z"
    )


def extract_assignments(root, *keys):
    assignments = list(
        filter(lambda x: isinstance(x, ast.Assign) and x.targets, root.body)
    )

    def extract_target_ids(node):
        return list(
            map(lambda x: x.id, filter(lambda x: isinstance(x, ast.Name), node.targets))
        )

    result = dict()
    for key in keys:
        for a in reversed(assignments):
            targets = extract_target_ids(a)
            if key in targets:
                if isinstance(a.value, ast.Str):
                    result[key] = a.value.s

                elif (
                    isinstance(a.value, ast.Call)
                    and hasattr(a.value, "func")
                    and a.value.func.id == "gettext"
                    and a.value.args
                    and isinstance(a.value.args[0], ast.Str)
                ):
                    result[key] = a.value.args[0].s

                break
    return result


_plugin_stats_7d = dict()
_plugin_stats_30d = dict()


def prefetch_plugin_stats():
    global _plugin_stats_7d, _plugin_stats_30d

    resp = requests.get(PLUGINSTATS_7D_URL)
    _plugin_stats_7d = resp.json()

    resp = requests.get(PLUGINSTATS_30D_URL)
    _plugin_stats_30d = resp.json()


github_query_executor = concurrent.futures.ThreadPoolExecutor(max_workers=5, thread_name_prefix="github_query_executor")
github_queries = queue.Queue()

def github_query_worker(queries, out=print):
    global github_graphql_counter

    assert GITHUB_TOKEN is not None

    auth = "token " + GITHUB_TOKEN
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": auth,
    }

    try:
        out("~~ Executing batch of {} queries: {}".format(len(queries), ", ".join(["{user}/{repo}".format(**q) for q in queries])))
        graphql_queries = {}
        for index, query in enumerate(queries):
            key = "Q{}".format(index)
            q = key + ": " + GITHUB_GRAPHQL_QUERY.replace("{{user}}", query["user"]).replace(
                "{{repo}}", query["repo"]
            )
            graphql_queries[key] = q

        payload = "query {\n" + "\n".join(graphql_queries.values()) + "\n}"

        github_graphql_counter += 1
        response = requests.post(
            GITHUB_GRAPHQL_URL, headers=headers, json={"query": payload}
        )
        out(
            "~~ Ratelimit: {}/{}".format(
                response.headers.get("X-Ratelimit-Remaining", "?"),
                response.headers.get("X-Ratelimit-Limit", "?"),
            )
        )
        response.raise_for_status()

        data = response.json()
        if not data:
            out(
                "!! No data available from Github API",
                file=sys.stderr,
            )
            return

        for index, query in enumerate(queries):
            key = "Q{}".format(index)
            result = data["data"].get(key, None)
            query["future"].set_result(result)

    except:
        out(
            "!! Error while reading and parsing data from Github API",
            file=sys.stderr,
        )
        trace = traceback.format_exc()
        for line in trace.split("\n"):
            out("!! " + line, file=sys.stderr)
        for query in queries:
            query["future"].set_result(None)


def github_batcher(out=print):
    queries = []
    while True:
        while len(queries) < BATCH_SIZE:
            try:
                queries.append(github_queries.get(timeout=1))
            except queue.Empty:
                break

        if queries:
            github_query_executor.submit(github_query_worker, queries, out=out)
        queries = []


def github_data(user, repo, out=print):
    global github_rest_counter

    if GITHUB_TOKEN is None:
        # GraphQL API does only work with a token
        return dict()

    auth = "token " + GITHUB_TOKEN
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": auth,
    }

    future = concurrent.futures.Future()
    github_queries.put({"user":user, "repo":repo, "future":future})
    out("Enqueued query for {}/{}".format(user, repo))

    repository_values = future.result(timeout=30)
    if not repository_values:
        return dict()

    release_count = repository_values["lastRelease"]["totalCount"]
    result = dict(
        repo="{}/{}".format(user, repo),
        open_issues=repository_values["openIssues"]["totalCount"],
        closed_issues=repository_values["closedIssues"]["totalCount"],
        releases=release_count,
        watchers=repository_values["watchers"]["totalCount"],
        stars=repository_values["stargazers"]["totalCount"],
        last_push=to_date(
            repository_values["lastPush"]["target"]["history"]["edges"][0]["node"][
                "committedDate"
            ]
        ),
    )

    if release_count:
        latest_release = repository_values["lastRelease"]["nodes"][0]
        if not latest_release["isPrerelease"]:
            result.update(
                latest_release=latest_release["name"],
                latest_release_date=to_date(latest_release["publishedAt"]),
                latest_release_url=latest_release["url"],
                latest_release_tag=latest_release["tagName"],
            )

        else:
            # latest release available via graphql is a prerelease, we need to use the REST API to get
            # the latest full release as we can't (yet?) filter for that on the graphql API
            out(
                "Latest release from GraphQL API is a prerelease, fetching latest via REST API"
            )

            try:
                url = GITHUB_REST_URL + "/repos/{}/{}/releases/latest".format(
                    user, repo
                )

                github_rest_counter += 1
                r = requests.get(url, headers=headers)
                out(
                    "~~ Ratelimit: {}/{}".format(
                        r.headers.get("X-Ratelimit-Remaining", "?"),
                        r.headers.get("X-Ratelimit-Limit", "?"),
                    )
                )
                r.raise_for_status()

                release = r.json()
                result.update(
                    latest_release=release["name"],
                    latest_release_date=to_date(release["published_at"]),
                    latest_release_url=release["html_url"],
                    latest_release_tag=release["tag_name"],
                )
            except Exception as exc:
                if hasattr(exc, "status_code") and exc.status_code != 404:
                    out(
                        "!! Error while retrieving latest release info from Github API for {}/{}, setting release count to 0: {}".format(
                            user, repo, exc
                        ),
                        file=sys.stderr,
                    )
                else:
                    out(
                        "No latest public release available, setting release count to 0"
                    )
                result.update(releases=0)

    return result


def extract_github_repo(url, out=print):
    if url is None or not url.startswith(GITHUB_PREFIX):
        return None, None

    if GITHUB_TOKEN is not None:
        auth = "token " + GITHUB_TOKEN
        headers = {"Authorization": auth}
    else:
        headers = None

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except Exception as exc:
        out("!! Error while fetching source URL: {}".format(exc))
        if isinstance(exc, requests.HTTPError) and exc.response.status_code == 500:
            # looks like a github hiccup, we hope for the best that this repo wasn't moved at some point and just
            # use the existing URL for further processing
            pass
        else:
            return None, None
    else:
        url = r.url
        if not url.startswith(GITHUB_PREFIX):
            return None, None

    parts = url[len(GITHUB_PREFIX) :].split("/")
    return parts[0], parts[1]


def extract_plugin_control_properties(user, repo, out=print):
    if GITHUB_TOKEN is not None:
        auth = "token " + GITHUB_TOKEN
        headers = {"Authorization": auth}
    else:
        headers = None

    def get_content(path):
        global github_rest_counter
        url = GITHUB_REST_URL + "/repos/{}/{}/contents/{}".format(user, repo, path)
        try:
            github_rest_counter += 1
            r = requests.get(url, headers=headers)
            out(
                "~~ Ratelimit: {}/{}".format(
                    r.headers.get("X-Ratelimit-Remaining", "?"),
                    r.headers.get("X-Ratelimit-Limit", "?"),
                )
            )
            r.raise_for_status()
        except Exception as exc:
            out(
                "!! Could not fetch contents for {}/{}:{}: {}".format(
                    user, repo, path, exc
                )
            )
            return None

        data = r.json()
        if "content" not in data:
            out("!! Could not fetch contents for {}/{}:{}".format(user, repo, path))
            return None

        try:
            content = base64.b64decode(data["content"])
        except Exception as exc:
            out(
                "!! Could not fetch contents for {}/{}:{}: {}".format(
                    user, repo, path, exc
                )
            )
            return None

        return content

    content_setup_py = get_content("setup.py")
    if not content_setup_py:
        return dict()

    try:
        root = ast.parse(content_setup_py, "setup.py")
    except Exception as exc:
        # invalid
        out(
            "!! Got an error while trying to build AST for setup.py from {}/{}:setup.py: {}".format(
                user, repo, exc
            )
        )
        return dict()

    props = extract_assignments(root, "plugin_identifier", "plugin_package")

    package = props.get("plugin_package")
    if package is None:
        if "plugin_identifier" in props:
            package = "octoprint_{}".format(props["plugin_identifier"])
        else:
            out(
                "!! Could not extract plugin package from {}/{}:setup.py".format(
                    user, repo
                )
            )
            return dict()

    path = "{}/__init__.py".format(package)
    out("__init__.py should be at {}/{}:{}".format(user, repo, path))

    content_init_py = get_content(path)
    if not content_init_py:
        return dict()

    try:
        root = ast.parse(content_init_py, path)
    except Exception as exc:
        # invalid
        out(
            "!! Got an error while trying to build AST for __init__.py from {}/{}:{}: {}".format(
                user, repo, path, exc
            )
        )
        return dict()

    return extract_assignments(
        root, "__plugin_pythoncompat__"
    )

def process_plugin_file(path, incl_stats=True, incl_github=True, incl_compat=True):
    global file_counter
    file_counter += 1

    result = []

    def out(line, prefix="", *args, **kwargs):
        result.append("{}{}".format(prefix, line))

    path_obj = Path(path)
    frontmatter, content = path_obj.read_text().lstrip().split("\n---", 1)
    frontmatter += "\n"

    data = ruamel.yaml.round_trip_load(frontmatter, preserve_quotes=True)
    clean = True
    plugin_id = data["id"]

    out("Processing plugin {} at path {}".format(plugin_id, path))

    if incl_stats:
        attributes = data.get("attributes", [])
        if attributes is None:
            attributes = []

        if "commercial" not in attributes:
            def build_stats(stats):
                result = dict(
                    instances=stats.get("instances", 0),
                    install_events=stats.get("install_events", 0),
                )
                if "versions" in stats:
                    result["versions"] = dict()
                    for version in stats["versions"]:
                        result["versions"][version] = stats["versions"][version]["instances"]

                return result

            data["stats"] = {
                "week": dict(instances=0, install_events=0),
                "month": dict(instances=0, install_events=0),
            }

            stats7d = _plugin_stats_7d["plugins"].get(data["id"].lower())
            if stats7d is not None:
                out("  Enriching {} with stats for week...".format(plugin_id))
                data["stats"]["week"] = build_stats(stats7d)
                clean = False

            stats30d = _plugin_stats_30d["plugins"].get(data["id"].lower())
            if stats30d is not None:
                out("  Enriching {} with stats for month...".format(plugin_id))
                data["stats"]["month"] = build_stats(stats30d)
                clean = False
        
        else:
            out("  Plugin is marked as commercial, skipping stats")

    if "github" in data and "repo" in data["github"]:
        user, repo = data["github"]["repo"].split("/")
    else:
        out("  Looking up github repo")
        user, repo = extract_github_repo(
            data.get("source"), out=functools.partial(out, prefix="    ")
        )

    if incl_github and user and repo:
        out(
            "  Loading github repo information for plugin {}: {}/{}".format(
                plugin_id, user, repo
            )
        )
        github = github_data(user, repo, out=functools.partial(out, prefix="    "))
        if github:
            out("  Enriching {} with github data...".format(plugin_id))
            data["github"] = github
            clean = False

    if incl_compat and user and repo:
        if "compatibility" not in data or "python" not in data["compatibility"]:
            # let's try to determine python compatibility from the actual plugin
            out(
                "  Extracting plugin control properties for plugin {} from {}/{}".format(
                    plugin_id, user, repo
                )
            )
            properties = extract_plugin_control_properties(
                user, repo, out=functools.partial(out, prefix="    ")
            )
            if "__plugin_pythoncompat__" in properties:
                if "compatibility" not in data:
                    data["compatibility"] = dict()
                data["compatibility"]["python"] = properties[
                    "__plugin_pythoncompat__"
                ]
                clean = False
                out("  Added python compatibility info from source")

    if not clean:
        with open(path, "w") as f:
            f.write("---\n")
            ruamel.yaml.round_trip_dump(data, f, indent=2, block_seq_indent=None)
            f.write("---")
            f.write(content)

    return "\n".join(result)


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=BATCH_SIZE, thread_name_prefix="process_worker")
    prefetch_plugin_stats()

    filtered = []
    if len(sys.argv) > 1:
        filtered = sys.argv[1:]

    no_stats = "--no-stats" in filtered
    no_github = "--no-github" in filtered
    no_compat = "--no-compat" in filtered

    filtered = [x for x in filtered if not x.startswith("--")]

    futures_to_name = dict()

    plugin_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "_plugins"
    )

    batcher = threading.Thread(target=github_batcher, name="github_batcher")
    batcher.daemon = True
    batcher.start()

    with os.scandir(plugin_dir) as it:
        for entry in it:
            if not entry.is_file() or not entry.name.endswith(".md"):
                continue
            if filtered and entry.name[:-3] not in filtered:
                continue
            future = executor.submit(process_plugin_file, entry.path, incl_stats=not no_stats, incl_github=not no_github, incl_compat=not no_compat)
            futures_to_name[future] = entry.name

    for future in concurrent.futures.as_completed(futures_to_name):
        name = futures_to_name[future]
        try:
            print(future.result())
            print("")
        except Exception as exc:
            print("{} generated an exception: {}".format(name, exc))

    print("Processed {} files".format(file_counter))
    print("  Used {} GitHub GraphQL calls".format(github_graphql_counter))
    print("  Used {} GitHub REST calls".format(github_rest_counter))
