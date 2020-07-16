# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import frontmatter
import colorama
import datetime
import pkg_resources
import click
import subprocess

from voluptuous import Schema, Invalid, Required, Optional, Any, All, Length, Range, Url

import os
import codecs
import sys

NonEmptyString = All(str, Length(min=1))

def Version(v):
	if not isinstance(v, str):
		raise Invalid("version {!r} is not a string".format(v))

	try:
		compat = v
		if not any(compat.startswith(c) for c in ("<", "<=", "!=", "==", ">=", ">", "~=", "===")):
			compat = ">={}".format(compat)
		pkg_resources.Requirement.parse("Foo" + compat)
	except:
		raise Invalid("version {} is not a valid PEP440 version specifier".format(v))

def Path(v):
	if not isinstance(v, str):
		raise Invalid("path {!r} is not a string".format(v))
	if not v.startswith("/assets/img/plugins/"):
		raise Invalid("path {} must start with /assets/img/plugins/".format(v))

def ImageLocation(v):
	if not isinstance(v, str):
		raise Invalid("image location {!r} is not a string".format(v))
	if len(v) == 0:
		raise Invalid("image location must be a non empty string")
	try:
		Url()(v)
	except Invalid:
		if not v.startswith("/assets/img/plugins/"):
			raise Invalid("image location '{}' must either be an URL or a path starting with /assets/img/plugins/".format(v))

ScreenshotDef = Schema({
	Required("url"): ImageLocation,
	Optional("alt"): NonEmptyString,
	Optional("caption"): NonEmptyString
})

Compatibility = Schema({
	Optional("octoprint"): [Version],
	Optional("os"): ["windows", "linux", "macos", "freebsd", "posix", "nix"],
	Optional("python"): Version
})

SCHEMA = Schema({
	Required("layout"): "plugin",
	Required("id"): NonEmptyString,
	Required("title"): NonEmptyString,
	Required("description"): NonEmptyString,
	Required("author"): NonEmptyString,
	Required("license"): NonEmptyString,

	Required("date"): datetime.date,

	Required("homepage"): Url(),
	Required("source"): Url(),
	Required("archive"): Url(),

	Optional("follow_dependency_links"): bool,

	Optional("tags"): list,
	Optional("screenshots"): All([ScreenshotDef]),
	Optional("featuredimage"): ImageLocation,
	Optional("compatibility"): Compatibility,

	Optional("disabled"): NonEmptyString,
	Optional("abandoned"): NonEmptyString,
	Optional("up_for_adoption"): Url(),
	Optional("redirect_from"): NonEmptyString
})

def validate_schema(data):
	SCHEMA(data)

def validate_id_match(data, path):
	if data["id"] != os.path.basename(path)[:-3]:
		raise ValueError("id {} for {} does not match file name".format(data["id"], path))

def validate_date_unchanged(data, path, cwd, sha):
	gitpath = path[len(cwd) + 1:]
	if sys.platform == "win32":
		gitpath = gitpath.replace("\\", "/")

	try:
		output = subprocess.check_output("git show {}:{}".format(sha, gitpath), encoding="utf-8")
		if not output:
			raise ValueError("could not read prior version")
	except subprocess.CalledProcessError:
		return

	old_metadata, old_content = frontmatter.parse(output)
	if data["date"] != old_metadata.get("date"):
		raise ValueError("date must not be changed after initial registration")

def validate(cwd, path, id_match=False, date_unchanged=False):
	with codecs.open(path, mode="r", encoding="utf-8") as f:
		metadata, content = frontmatter.parse(f.read())
	SCHEMA(metadata)

	if id_match:
		validate_id_match(metadata, path)

	if date_unchanged and path.startswith(cwd):
		validate_date_unchanged(metadata, path, cwd, date_unchanged)

@click.command()
@click.option("--debug", is_flag=True)
@click.option("--id-match", "id_match", is_flag=True)
@click.option("--date-unchanged", "date_unchanged", help="Provide git committish with which to compare")
@click.argument("paths", nargs=-1)
def main(paths, debug, id_match, date_unchanged):
	count = 0
	fails = 0

	paths = list(map(os.path.abspath, paths))

	cwd = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
	plugin_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_plugins"))
	with os.scandir(plugin_dir) as it:
		for entry in it:
			if not entry.is_file() or not entry.name.endswith(".md"):
				continue

			path = entry.path
			if paths and path not in paths:
				continue

			try:
				validate(cwd, path,
				         id_match=id_match,
				         date_unchanged=date_unchanged)
			except Exception as exc:
				print("{}: ".format(path), end="")
				print(colorama.Fore.RED + colorama.Style.BRIGHT + "FAIL")
				print("  " + str(exc))
				fails += 1
			else:
				if debug:
					print("{}: ".format(path), end="")
					print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "PASS")

			count += 1

	print("Validated {} files, {} passes, {} fails".format(count, count - fails, fails))
	if fails != 0:
		sys.exit(-1)

if __name__ == "__main__":
	colorama.init(autoreset=True)
	main()

