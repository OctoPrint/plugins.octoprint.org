# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import frontmatter

import os
import sys
import traceback
import concurrent.futures
import base64
import ast
import functools

from datetime import datetime

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)

PLUGINSTATS_7D_URL = "https://data.octoprint.org/export/plugin_stats_7d.json"
PLUGINSTATS_30D_URL = "https://data.octoprint.org/export/plugin_stats_30d.json"

GITHUB_PREFIX = "https://github.com/"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
GITHUB_GRAPHQL_QUERY = """
query {
  repository(owner: \"{{user}}\", name: \"{{repo}}\") {
    openIssues: issues(states: OPEN) {
      totalCount
    },
    closedIssues: issues(states: CLOSED) {
      totalCount
    },
    releasesCount: releases(last: 100){
      totalCount
    },
    lastRelease: releases(last:1){
       nodes {
        name,
        publishedAt,
        url
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
    watchers(last:100){
      totalCount
    },
    stargazers(last:100){
      totalCount
    }
  }
}"""

GITHUB_REST_URL = "https://api.github.com"

def to_date(date_str):
	return datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S %z")

_plugin_stats_7d = dict()
_plugin_stats_30d = dict()

def prefetch_plugin_stats():
	global _plugin_stats_7d, _plugin_stats_30d

	resp = requests.get(PLUGINSTATS_7D_URL)
	_plugin_stats_7d = resp.json()

	resp = requests.get(PLUGINSTATS_30D_URL)
	_plugin_stats_30d = resp.json()

def github_data(user, repo, out=print):
	if GITHUB_TOKEN is not None:
		auth = "token "  + GITHUB_TOKEN
	else:
		return dict()

	graph_ql_query = GITHUB_GRAPHQL_QUERY\
		.replace("{{user}}", user)\
		.replace("{{repo}}", repo)

	try:
		response = requests.post(GITHUB_GRAPHQL_URL,
		                         headers={"Content-Type": "application/json; charset=utf-8",
		                                  "Authorization": auth},
		                         json={'query': graph_ql_query})

		if response.status_code != 200:
			out("!! Error while querying Github API for {}/{}, status: {}, body: {}".format(user, repo, response.status_code, response.text), file=sys.stderr)
			return dict()

		data = response.json()
		if not data:
			out("!! No data available from Github API for {}/{}".format(user, repo), file=sys.stderr)
			return dict()

		repository_values = data["data"]["repository"]
		release_count = repository_values["releasesCount"]["totalCount"]
		result = dict(repo="{}/{}".format(user, repo),
		              open_issues=repository_values["openIssues"]["totalCount"],
		              closed_issues=repository_values["closedIssues"]["totalCount"],
		              releases=release_count,
		              watchers=repository_values["watchers"]["totalCount"],
		              stars=repository_values["stargazers"]["totalCount"],
		              last_push=to_date(repository_values["lastPush"]["target"]["history"]["edges"][0]["node"]["committedDate"]))

		if release_count:
			latest_release = repository_values["lastRelease"]["nodes"][0]
			result.update(latest_release = latest_release["name"],
			              latest_release_date=to_date(latest_release["publishedAt"]),
			              latest_release_url=latest_release["url"])

		out("~~ Ratelimit: {}/{}".format(response.headers.get("X-Ratelimit-Remaining", "?"),
		                                 response.headers.get("X-Ratelimit-Limit", "?")))

		return result
	except:
		out("!! Error while reading and parsing data from Github API for {}/{}".format(user, repo), file=sys.stderr)
		traceback.print_exc()
		return dict()

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
		out("~~ Ratelimit: {}/{}".format(r.headers.get("X-Ratelimit-Remaining", "?"),
		                                 r.headers.get("X-Ratelimit-Limit", "?")))
	except Exception as exc:
		out("!! Error while fetching source URL: {}".format(exc))
		return None, None

	url = r.url
	if not url.startswith(GITHUB_PREFIX):
		return None, None


	parts = url[len(GITHUB_PREFIX):].split("/")
	return parts[0], parts[1]

def extract_plugin_control_properties(user, repo, out=print):
	if GITHUB_TOKEN is not None:
		auth = "token " + GITHUB_TOKEN
		headers = {"Authorization": auth}
	else:
		headers = None

	result = dict()

	url = GITHUB_REST_URL + "/search/code?q=(__plugin_implementation__+OR+__plugin_hooks__)+repo:{user}/{repo}+in:file+filename:__init__.py".format(user=user, repo=repo)
	try:
		r = requests.get(url, headers=headers)
		r.raise_for_status()
		out("~~ Ratelimit: {}/{}".format(r.headers.get("X-Ratelimit-Remaining", "?"),
		                                 r.headers.get("X-Ratelimit-Limit", "?")))
	except Exception as ex:
		out("!! Got an error while trying to search for __init__.py on {}/{}: {}".format(user, repo, ex))
		return result

	data = r.json()

	if "items" not in data:
		out("!! Got no results for __init__.py in {}/{}, can't extract plugin properties: {}, {!r}".format(user, repo, r.status_code, data))
		return result

	paths = set()
	for item in data["items"]:
		paths.add((item["url"], item["path"]))

	if len(paths) != 1:
		out("!! Got none or more than one result for __init__.py in {}/{}, can't extract plugin properties: {!r}".format(user, repo, paths))
		return result

	url, path = paths.pop()

	out("Found path of __init__.py: {}".format(path))

	try:
		r = requests.get(url, headers=headers)
		r.raise_for_status()
		out("~~ Ratelimit: {}/{}".format(r.headers.get("X-Ratelimit-Remaining", "?"),
		                                 r.headers.get("X-Ratelimit-Limit", "?")))
	except Exception as exc:
		out("!! Got an error while trying to read contents of __init__.py from {}/{}:{}: {}".format(user, repo, path, exc))
		return result

	data = r.json()

	try:
		content = base64.b64decode(data.get("content", ""))
		root = ast.parse(content, "__init__.py")
	except Exception as exc:
		# invalid
		out("!! Got an error while trying to build AST for __init__.py from {}/{}:{}: {}".format(user, repo, path, exc))
		return result

	assignments = list(filter(lambda x: isinstance(x, ast.Assign) and x.targets,
	                          root.body))

	def extract_target_ids(node):
		return list(map(lambda x: x.id,
		                filter(lambda x: isinstance(x, ast.Name), node.targets)))

	for key in ("__plugin_pythoncompat__",):
		for a in reversed(assignments):
			targets = extract_target_ids(a)
			if key in targets:
				if isinstance(a.value, ast.Str):
					result[key] = a.value.s

				elif isinstance(a.value, ast.Call) and hasattr(a.value, "func") \
						and a.value.func.id == "gettext" and a.value.args \
						and isinstance(a.value.args[0], ast.Str):
					result[key] = a.value.args[0].s

				break

	return result

def process_plugin_file(path, incl_stats=True, incl_github=True):
	result = []
	def out(line, prefix="", *args, **kwargs):
		result.append("{}{}".format(prefix, line))

	data = frontmatter.load(path)
	plugin_id = data["id"]

	out("Processing plugin {} at path {}".format(plugin_id, path))

	if incl_stats:
		def build_stats(stats):
			result = dict(instances=stats.get("instances", 0),
			              install_events=stats.get("install_events", 0))
			if "versions" in stats:
				result["versions"] = dict()
				for version in stats["versions"]:
					result["versions"][version] = stats["versions"][version]["instances"]

			return result

		data["stats"] = {"week": dict(instances=0,
		                              install_events=0),
		                 "month": dict(instances=0,
		                               install_events=0)}

		stats7d = _plugin_stats_7d.get(data["id"].lower())
		if stats7d is not None:
			out("  Enriching {} with stats for week...".format(plugin_id))
			data["stats"]["week"] = build_stats(stats7d)

		stats30d = _plugin_stats_30d.get(data["id"].lower())
		if stats30d is not None:
			out("  Enriching {} with stats for month...".format(plugin_id))
			data["stats"]["month"] = build_stats(stats30d)

	if incl_github:
		if "github" in data and "repo" in data["github"]:
			user, repo = data["github"]["repo"].split("/")
		else:
			user, repo = extract_github_repo(data.get("source"), out=functools.partial(out, prefix="    "))

		if user and repo:
			out("  Loading github repo information for plugin {}: {}/{}".format(plugin_id, user, repo))
			github = github_data(user, repo, out=functools.partial(out, prefix="    "))
			if github:
				out("  Enriching {} with github data...".format(plugin_id))
				data["github"] = github

			if "compatibility" not in data or "python" not in data["compatibility"]:
				# let's try to determine python compatibility from the actual plugin
				out("  Extracting plugin control properties for plugin {} from {}/{}".format(plugin_id, user, repo))
				properties = extract_plugin_control_properties(user, repo, out=functools.partial(out, prefix="    "))
				if "__plugin_pythoncompat__" in properties:
					if "compatibility" not in data:
						data["compatibility"] = dict()
					data["compatibility"]["python"] = properties["__plugin_pythoncompat__"]

	with open(path, "wb") as f:
		frontmatter.dump(data, f)

	return "\n".join(result)

if __name__ == "__main__":
	executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
	prefetch_plugin_stats()

	filtered = None
	if len(sys.argv) > 1:
		filtered = sys.argv[1:]

	futures_to_name = dict()

	plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_plugins")
	with os.scandir(plugin_dir) as it:
		for entry in it:
			if not entry.is_file() or not entry.name.endswith(".md"):
				continue
			if filtered and entry.name[:-3] not in filtered:
				continue
			future = executor.submit(process_plugin_file, entry.path)
			futures_to_name[future] = entry.name

	for future in concurrent.futures.as_completed(futures_to_name):
		name = futures_to_name[future]
		try:
			print(future.result())
			print("")
		except Exception as exc:
			print("{} generated an exception: {}".format(name, exc))
