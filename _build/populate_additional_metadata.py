# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import frontmatter

import os
import sys
import traceback
import concurrent.futures

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

		return result
	except:
		out("!! Error while reading and parsing data from Github API for {}/{}".format(user, repo), file=sys.stderr)
		traceback.print_exc()
		return dict()

def extract_github_repo(url):
	if url is None or not url.startswith(GITHUB_PREFIX):
		return None, None

	r = requests.get(url)
	url = r.url
	if not url.startswith(GITHUB_PREFIX):
		return None, None

	parts = url[len(GITHUB_PREFIX):].split("/")
	return parts[0], parts[1]

def process_plugin_file(path, incl_stats=True, incl_github=True):
	result = []
	def out(line, *args, **kwargs):
		result.append(line)

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
			user, repo = extract_github_repo(data.get("source"))

		if user and repo:
			out("  Loading github repo information for plugin {}: {}/{}".format(plugin_id, user, repo))
			github = github_data(user, repo)
			if github:
				out("  Enriching {} with github data...".format(plugin_id))
				data["github"] = github

	with open(path, "wb") as f:
		frontmatter.dump(data, f)

	return "\n".join(result)

if __name__ == "__main__":
	executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
	prefetch_plugin_stats()

	futures_to_name = dict()

	plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_plugins")
	with os.scandir(plugin_dir) as it:
		for entry in it:
			if not entry.is_file() or not entry.name.endswith(".md"):
				continue
			future = executor.submit(process_plugin_file, entry.path, incl_github=GITHUB_TOKEN is not None)
			futures_to_name[future] = entry.name

	for future in concurrent.futures.as_completed(futures_to_name):
		name = futures_to_name[future]
		try:
			print(future.result())
			print("")
		except Exception as exc:
			print("{} generated an exception: {}".format(name, exc))
