#!/usr/bin/env python
"""Generate ``syntax.json``."""
import json
import sys
from urllib import request

from bs4 import BeautifulSoup, FeatureNotFound


def main(output: str = ""):
    """Generete ``syntax.json``.

    :param output:
    :type output: str
    """
    with request.urlopen(
        "https://www.sublimetext.com/docs/scope_naming.html"
    ) as f:
        html = f.read()

    try:
        soup = BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")

    items = []
    reference = soup.find(id="alphabetical-reference")
    for section in reference.findAll("section"):  # type: ignore
        top = section.get("id")
        for ul in section.findAll("ul"):
            p = ul
            while p.name != "p":
                p = p.previous_sibling
            info = p.get_text()
            for li in ul.findAll("li"):
                word = li.get_text()
                if word.split(".")[0] != top:
                    continue
                items += [{"word": word, "info": info}]

    if output == "-" or len(sys.argv) < 1:
        json.dump(items, sys.stdout)
    else:
        with open(sys.argv[1], "w") as f:
            json.dump(items, f)


if __name__ == "__main__":
    main()
