r"""Api
=======
"""
import os
import re
from gzip import decompress

from markdown_it import MarkdownIt
from platformdirs import site_data_dir
from pypandoc import convert_text


def init_document() -> dict[str, str]:
    r"""Init document.

    :rtype: dict[str, str]
    """
    with open(
        os.path.join(
            os.path.join(site_data_dir("man"), "man5"), "zathurarc.5.gz"
        ),
        "rb",
    ) as f:
        text = decompress(f.read()).decode()
    text = convert_text(text, "markdown", "man")
    md = MarkdownIt("commonmark", {})
    tokens = md.parse(text)
    indices = []
    end_index = len(tokens)
    for i, token in enumerate(tokens):
        if token.content == "OPTIONS":
            end_index = i
            break
        if token.tag == "h2" and token.type == "heading_open":
            indices += [i + 1]
    items = {}
    for i, index in enumerate(indices):
        keyword, _, items[keyword] = tokens[index].content.partition(" - ")
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        for token in tokens[index + 1 : index2]:
            if token.content != "" and not token.content.startswith("<!--"):
                items[keyword] += "\n" + re.sub(r"\n\s*", " ", token.content)

    indices = []
    for i, token in enumerate(tokens[end_index:], end_index):
        if token.content == "SEE ALSO":
            end_index = i
            break
        if (
            token.type == "inline"
            and token.content.islower()
            and token.content.startswith("***")
            and token.content.endswith("***")
        ):
            indices += [i]
    for i, index in enumerate(indices):
        keyword = tokens[index].content.strip("*")
        items[keyword] = ""
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        for token in tokens[index + 1 : index2]:
            if (
                token.content != ""
                and not token.content.startswith("<!--")
                and token.content != ":"
            ):
                items[keyword] += "\n" + re.sub(
                    r"\n\s*", " ", token.content.replace("\n\n", "---")
                ).replace("---", "\n")
        items[keyword] = items[keyword].strip()

    return items
