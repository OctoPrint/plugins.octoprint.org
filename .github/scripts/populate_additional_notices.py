import concurrent.futures
import os
import sys
from datetime import datetime

import frontmatter
import requests
import yaml

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)

GITHUB_REST_URL = "https://api.github.com"


def to_date(date_str):
    return datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime(
        "%Y-%m-%d %H:%M:%S%z"
    )


def get_issue(user, repo, issue):
    if GITHUB_TOKEN is not None:
        auth = "token " + GITHUB_TOKEN
        headers = {"Authorization": auth}
    else:
        headers = None

    r = requests.get(
        GITHUB_REST_URL + "/repos/" + user + "/" + repo + "/issues/" + issue,
        headers=headers,
    )
    r.raise_for_status()
    return r.json()


def process_plugin_file(path):
    output = []

    def out(line, prefix="", *args, **kwargs):
        output.append("{}{}".format(prefix, line))

    notices = []

    data = frontmatter.load(path)
    plugin_id = data["id"]

    out("Processing plugin {} at path {}".format(plugin_id, path))

    if data.get("abandoned"):
        # plugin is marked as abandoned, determine date to include in notification
        url = data["abandoned"]

        if url.startswith("https://github.com"):
            # github issue?
            parts = url.split("/")
            if len(parts) == 7 and parts[5] == "issues":
                user = parts[3]
                repo = parts[4]
                issue = parts[6]

                out(
                    "Abandonment URL seems to be Github ticket {}/{}#{}".format(
                        user, repo, issue
                    )
                )
                issue_data = get_issue(user, repo, issue)

                creation_date = to_date(issue_data["created_at"])
                out("Ticket was created on {}".format(creation_date))

                notices.append(
                    dict(
                        plugin=plugin_id,
                        date=creation_date,
                        text='This plugin has been abandoned by its maintainer and is looking for someone to adopt it. If you want to step in as the new maintainer please get in touch at the "Read more..." link below.',
                        link=url,
                    )
                )
                out(
                    "Generated abandonment/adoption notice dated {} and pointing at {}".format(
                        creation_date, url
                    )
                )

    return "\n".join(output), notices


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    filtered = None
    if len(sys.argv) > 1:
        filtered = sys.argv[1:]

    futures_to_name = dict()

    plugin_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "_plugins"
    )
    with os.scandir(plugin_dir) as it:
        for entry in it:
            if not entry.is_file() or not entry.name.endswith(".md"):
                continue
            if filtered and entry.name[:-3] not in filtered:
                continue
            future = executor.submit(process_plugin_file, entry.path)
            futures_to_name[future] = entry.name

    notices = []
    for future in concurrent.futures.as_completed(futures_to_name):
        name = futures_to_name[future]
        try:
            output, result = future.result()
            notices += result

            print(output)
            print("")
        except Exception as exc:
            print("{} generated an exception: {}".format(name, exc))

    if notices:
        # there were notices added, write them to the data file now
        notice_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "..",
            "_data",
            "notices.yaml",
        )

        print("Adding {} new notices to {}...".format(len(notices), notice_path))

        with open(notice_path, "r") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, list)
        data += notices
        with open(notice_path, "w") as f:
            yaml.safe_dump(data, f)

        print("Notices added.")
