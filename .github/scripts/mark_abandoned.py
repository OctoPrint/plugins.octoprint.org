# -*- coding: utf-8 -*-
import codecs

import click
import colorama


def mark_abandoned(path, ticket, force=False):
    with codecs.open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    in_frontmatter = False
    armed = True
    updated_lines = []
    for line in lines:
        if armed:
            if line.strip() == "---":
                if in_frontmatter:
                    # end of frontmatter, do our thing now
                    updated_lines.append("abandoned: {}\n".format(ticket))
                    armed = False
                in_frontmatter = not in_frontmatter
            elif in_frontmatter and line.startswith("abandoned:"):
                if force:
                    continue
                else:
                    print(
                        colorama.Fore.RED
                        + colorama.Style.BRIGHT
                        + "{} is already marked as abandoned!".format(path)
                    )
                    return

        updated_lines.append(line)

    with codecs.open(path, mode="w", encoding="utf-8") as f:
        for line in updated_lines:
            f.write(line)
    print(
        colorama.Fore.GREEN
        + colorama.Style.BRIGHT
        + "{} marked as abandoned".format(path)
    )


def mark_unabandoned(path):
    with codecs.open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    in_frontmatter = False
    armed = True
    updated_lines = []
    for line in lines:
        if armed:
            if line.strip() == "---":
                if in_frontmatter:
                    armed = False
                in_frontmatter = not in_frontmatter
            elif in_frontmatter and line.startswith("abandoned:"):
                continue
        updated_lines.append(line)

    with codecs.open(path, mode="w", encoding="utf-8") as f:
        for line in updated_lines:
            f.write(line)
    print(
        colorama.Fore.GREEN
        + colorama.Style.BRIGHT
        + "{} unmarked as abandoned".format(path)
    )


@click.command()
@click.option("--unmark", is_flag=True)
@click.option("--force", is_flag=True)
@click.argument("path")
@click.argument("ticket", default=None)
def main(unmark, force, path, ticket):
    if unmark:
        mark_unabandoned(path)
    else:
        mark_abandoned(path, ticket, force=force)


if __name__ == "__main__":
    colorama.init(autoreset=True)
    main()
