# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import frontmatter

import os
import time

from datetime import datetime

GITHUB_CREDENTIALS = os.environ.get("GITHUB_CREDENTIALS", None)

PLUGINSTATS_7D_URL = "https://data.octoprint.org/export/plugin_stats_7d.json"
PLUGINSTATS_30D_URL = "https://data.octoprint.org/export/plugin_stats_30d.json"

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"

_plugin_stats_7d = None
_plugin_stats_30d = None

def plugin_stats_7d(plugin):
	global _plugin_stats_7d
	if _plugin_stats_7d is None:
		resp = requests.get(PLUGINSTATS_7D_URL)
		_plugin_stats_7d = resp.json()
	return _plugin_stats_7d.get(plugin)

def plugin_stats_30d(plugin):
	global _plugin_stats_30d
	if _plugin_stats_30d is None:
		resp = requests.get(PLUGINSTATS_30D_URL)
		_plugin_stats_30d = resp.json()
	return _plugin_stats_30d.get(plugin)

def github_data(user, repo):
	if GITHUB_CREDENTIALS is not None:
		auth = "token "  + GITHUB_CREDENTIALS
	else:
		print("No GitHub-Statistic, because no Token provided")
		return dict()

	graphQLQuery = """
query {
  repository(owner: \"""" +  user + """\", name: \"""" + repo + """\") {
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

	requested_url = GITHUB_GRAPHQL_URL

	response = requests.post(requested_url,
	                    	headers={
									"Content-Type": "application/json; charset=utf-8",
									"Authorization": auth
							},
							json={'query': graphQLQuery} )

	print_response_by_error(requested_url, response)
	response_json = response.json()

	github_statistics = dict()
	if (len(response_json) == 0):
		print("No JSON-Response available from github-api")
		return github_statistics

	repositoryValues = response_json.get("data").get("repository")
	github_statistics.update(open_issues = repositoryValues.get("openIssues").get("totalCount"))
	github_statistics.update(closed_issues = repositoryValues.get("closedIssues").get("totalCount"))
	releaseCount = repositoryValues.get("releasesCount").get("totalCount")
	github_statistics.update(releases = releaseCount)
	github_statistics.update(watchers = repositoryValues.get("watchers").get("totalCount"))
	github_statistics.update(stars = repositoryValues.get("stargazers").get("totalCount"))
	lastPush = repositoryValues.get("lastPush").get("target").get("history").get("edges")[0].get("node").get("committedDate")
	github_statistics.update(last_push = lastPush)

	if (releaseCount > 0):
		latestRelease = repositoryValues.get("lastRelease").get("nodes")[0]
		github_statistics.update(latest_release = latestRelease.get("name"))
		github_statistics.update(latest_release_date = latestRelease.get("publishedAt"))
		github_statistics.update(latest_release_url = latestRelease.get("url"))

	return github_statistics

def print_response_by_error(requestedURL, response):
	httpStatus = response.status_code
	if (httpStatus != 200):
		responseText = response.text
		print("Error for URL '" + requestedURL + "'")
		print("  Response-Status:'" + str(httpStatus) + "', Text:'" + responseText + "'")


def process_plugin_file(path, incl_stats=True, incl_github=True):
	data = frontmatter.load(path)
	plugin_id = data["id"]

	print("Processing plugin {} at path {}".format(plugin_id, path))

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

		stats7d = plugin_stats_7d(data["id"].lower())
		if stats7d is not None:
			print("  Enriching {} with stats for week...".format(plugin_id))
			data["stats"]["week"] = build_stats(stats7d)

		stats30d = plugin_stats_30d(data["id"].lower())
		if stats30d is not None:
			print("  Enriching {} with stats for month...".format(plugin_id))
			data["stats"]["month"] = build_stats(stats30d)

	if incl_github:
		user = repo = None
		if "github" in data and "repo" in data["github"]:
			user, repo = data["github"]["repo"].split("/")
		elif data.get("source", "").startswith("https://github.com/"):
			parts = data["source"][len("https://github.com/"):].split("/")
			user = parts[0]
			repo = parts[1]

		if user and repo:
			print("  Loading github repo information for plugin {}: {}/{}".format(plugin_id, user, repo))
			github = github_data(user, repo)
			if github:
				print("  Enriching {} with github data...".format(plugin_id))
				data ["github"] = github

	with open(path, "wb") as f:
		frontmatter.dump(data, f)

if __name__ == "__main__":
	plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_plugins")
	with os.scandir(plugin_dir) as it:
		for entry in it:
			if not entry.is_file() or not entry.name.endswith(".md"):
				continue
			process_plugin_file(entry.path,
			                    incl_github=GITHUB_CREDENTIALS is not None)
			print("")
			time.sleep(.2)