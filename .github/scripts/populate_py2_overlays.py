import concurrent.futures
import os
import sys

import frontmatter
import pkg_resources
import yaml


def process_plugin_file(path):
    output = []

    def out(line, prefix="", *args, **kwargs):
        output.append("{}{}".format(prefix, line))

    overlay = {}

    data = frontmatter.load(path)
    plugin_id = data["id"]

    out("Processing plugin {} at path {}".format(plugin_id, path))

    if data.get("compatibility", {}).get("python"):
        pycompat = data["compatibility"]["python"]
        s = pkg_resources.Requirement.parse("Python" + pycompat)
        if "2.7" not in s:
            out(
                "Plugin {} is not Python 2 compatible, disable update checks in the field".format(
                    plugin_id
                )
            )
            overlay = {plugin_id: {"enabled": False, "compatible": False}}

    return "\n".join(output), overlay


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    filtered = None
    if len(sys.argv) > 1:
        filtered = sys.argv[1:]

    futures_to_name = dict()

    overlays_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "..",
        "_data",
        "update_check_overlays_py2.yaml",
    )
    with open(overlays_path, "r") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict)

    plugin_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "_plugins"
    )
    with os.scandir(plugin_dir) as it:
        for entry in it:
            if not entry.is_file() or not entry.name.endswith(".md"):
                continue
            if filtered and entry.name[:-3] not in filtered:
                continue
            if entry.name[:-3] in data:
                continue
            future = executor.submit(process_plugin_file, entry.path)
            futures_to_name[future] = entry.name

    overlays = {}
    for future in concurrent.futures.as_completed(futures_to_name):
        name = futures_to_name[future]
        try:
            output, result = future.result()
            overlays.update(result)

            print(output)
            print("")
        except Exception as exc:
            print("{} generated an exception: {}".format(name, exc))

    if overlays:
        # there were overlays added, write them to the data file now
        print("Adding {} new overlays to {}...".format(len(overlays), overlays_path))

        data.update(overlays)
        with open(overlays_path, "w") as f:
            yaml.safe_dump(data, f)

        print("Overlays added.")
