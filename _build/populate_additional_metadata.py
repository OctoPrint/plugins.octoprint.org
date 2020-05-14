# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import frontmatter

import os
import time

from datetime import datetime

GITHUB_CREDENTIALS = os.environ.get("GITHUB_CREDENTIALS", None)

PLUGINSTATS_URL = "https://data.octoprint.org/export/plugin_stats.json"
GITHUBREPO_URL = "https://api.github.com/repos/{user}/{repo}"

_plugin_stats = None

def plugin_stats(plugin):
	global _plugin_stats
	if _plugin_stats is None:
		resp = requests.get(PLUGINSTATS_URL)
		_plugin_stats = resp.json()
	return _plugin_stats.get(plugin)

def github_data(user, repo):
	if GITHUB_CREDENTIALS is not None:
		auth = tuple(GITHUB_CREDENTIALS.split(":"))
	else:
		auth = None

	resp = requests.get(GITHUBREPO_URL.format(user=user, repo=repo),
	                    auth=auth,
	                    headers={"Accept":"application/vnd.github.v3+json"})
	repodata = resp.json()

	return dict(stars=repodata.get("stargazers_count"),
	            watchers=repodata.get("watchers_count"),
	            issues=repodata.get("open_issues_count"),
	            last_push=datetime.fromisoformat(repodata.get("pushed_at").replace("Z", "+00:00")))

def process_plugin_file(path, incl_stats=True, incl_github=True):
	data = frontmatter.load(path)
	plugin_id = data["id"]

	print("Processing plugin {} at path {}".format(plugin_id, path))

	if incl_stats:
		stats = plugin_stats(data["id"].lower())
		if stats is not None:
			print("Enriching {} with stats...".format(plugin_id))
			data["stats"] = dict(installations=stats["instances"])
			if "versions" in stats:
				data["stats"]["versions"] = dict()
				for version in stats["versions"]:
					data["stats"]["versions"][version] = stats["versions"][version]["instances"]
		else:
			data["stats"] = dict(installations=0)

	if incl_github:
		user = repo = None
		if "github" in data and "repo" in data["github"]:
			user, repo = data["github"]["repo"].split("/")
		elif data.get("source", "").startswith("https://github.com/"):
			parts = data["source"][len("https://github.com/"):].split("/")
			user = parts[0]
			repo = parts[1]

		if user and repo:
			print("Found github repo information for plugin {}: {}/{}".format(plugin_id, user, repo))
			github = github_data(user, repo)
			if github:
				print("Enriching {} with github data...".format(path))
				data["github"] = dict(repo="{}/{}".format(user, repo),
				                      stars=github["stars"],
				                      watchers=github["watchers"],
				                      issues=github["issues"],
				                      last_push=github["last_push"].strftime("%Y-%m-%d %H:%M:%S %z"))

	with open(path, "wb") as f:
		frontmatter.dump(data, f)

if __name__ == "__main__":
	count = 0
	plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_plugins")
	with os.scandir(plugin_dir) as it:
		for entry in it:
			if not entry.is_file() or not entry.name.endswith(".md"):
				continue
			print("Processing {}...".format(entry.path))
			process_plugin_file(entry.path,
			                    incl_github=GITHUB_CREDENTIALS is not None)
			print("")
			time.sleep(1)

			count += 1
			#if count > 9:
			#	break