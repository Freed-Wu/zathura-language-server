#!/usr/bin/env python
"""Generate ``scope.json``."""
import json
import sys
from urllib import request

from bs4 import BeautifulSoup, FeatureNotFound
from bs4.element import Tag


def main(output: str = ""):
    """Generate ``scope.json``.

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
    if not isinstance(reference, Tag):
        sys.exit("alphabetical-reference is not Tag!")
    p = reference.find("p")
    if not isinstance(p, Tag):
        sys.exit("p is not Tag!")
    info = p.get_text().replace("\n", " ").strip()
    ul = reference.find("ul")
    if not isinstance(ul, Tag):
        sys.exit("ul is not Tag!")
    for li in ul.find_all("li"):
        word = li.get_text().strip(".")
        items += [{"word": word, "info": info, "menu": "scope"}]
    for section in reference.find_all("section"):
        top = section.get("id")
        for ul in section.find_all("ul"):
            p = ul.find_previous("p")
            info = p.get_text().replace("\n", " ").strip()
            for li in ul.find_all("li"):
                word = li.get_text()
                if word.split(".")[0] != top:
                    continue
                items += [{"word": word, "info": info, "menu": "scope"}]
    items.sort(key=lambda x: x["word"], reverse=True)

    if output == "-" or len(sys.argv) < 2:
        json.dump(items, sys.stdout)
    else:
        with open(sys.argv[1], "w") as f:
            json.dump(items, f)


if __name__ == "__main__":
    main()
