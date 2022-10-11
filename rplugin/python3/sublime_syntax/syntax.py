#!/usr/bin/env python
"""Generate ``syntax.json``."""
import json
import sys
from urllib import request

from bs4 import BeautifulSoup, FeatureNotFound


def main(output: str = ""):
    """Generate ``syntax.json``.

    :param output:
    :type output: str
    """
    with request.urlopen("http://www.sublimetext.com/docs/syntax.html") as f:
        html = f.read()

    try:
        soup = BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")
    items = []
    dls = soup.find_all("dl", class_="setting")
    for dl in dls:
        word = dl.find("span").get_text()
        info = dl.find("dd").get_text().replace("\n", " ").strip()
        items += [{"word": word, "info": info, "menu": "syntax"}]

    if output == "-" or len(sys.argv) < 2:
        json.dump(items, sys.stdout)
    else:
        with open(sys.argv[1], "w") as f:
            json.dump(items, f)


if __name__ == "__main__":
    main()
