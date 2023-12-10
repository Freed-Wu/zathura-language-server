r"""Zathurarc
=============
"""
from typing import Any

from tree_sitter_lsp.misc import get_md_tokens

from .._metainfo import SOURCE, project


def init_schema() -> dict[str, Any]:
    r"""Init schema.

    :rtype: dict[str, Any]
    """
    filetype = "zathurarc"
    schemas = {
        filetype: {
            "$id": f"{SOURCE}/blob/main/src/termux_language_server/assets/json/{filetype}.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$comment": (
                "Don't edit this file directly! It is generated by "
                f"`{project} --generate-schema={filetype}`."
            ),
            "type": "object",
            "additionalProperties": False,
            "properties": {},
        }
    }
    tokens = get_md_tokens("zathurarc")
    indices = []
    end_index = len(tokens)
    keys = []
    shortcuts = []
    arguments = []
    for i, token in enumerate(tokens):
        if token.content == "OPTIONS":
            end_index = i
            break
        if token.tag == "h2" and token.type == "heading_open":
            indices += [i + 1]
    for i, index in enumerate(indices):
        keyword, _, description = tokens[index].content.partition(" - ")
        schemas[filetype]["properties"][keyword] = {
            "type": "object",
        }
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        data = []
        for token in tokens[index + 1 : index2]:
            if len(data) == 2:
                break
            if token.content == "" or token.content.startswith("<!--"):
                continue
            data += [token.content]
        if keyword == "map":
            start = False
            for k, token in enumerate(tokens[index + 1 : index2], index + 1):
                if token.content.replace("*", "") in {
                    "Special keys",
                    "Mouse buttons",
                }:
                    keys += [
                        "<" + line.lstrip("> ").partition(" ")[0] + ">"
                        for line in tokens[k + 5].content.splitlines()
                    ][2:]
                if token.content.replace("*", "") == "Shortcut functions":
                    shortcuts = [
                        line.strip("- :").replace("*", " ").strip(" ")
                        for line in tokens[k + 5].content.splitlines()
                        if line.startswith("-   ")
                    ]
                if token.content.replace("*", "") == "Pass arguments":
                    start = True
                if (
                    start
                    and token.content.islower()
                    and token.type == "inline"
                ):
                    arguments += [token.content]
        schemas[filetype]["properties"][keyword][
            "description"
        ] = f"""# {description}
{data[0]}
```zathurarc
{data[1]}
```"""
    schemas[filetype]["properties"]["include"]["type"] = "array"
    schemas[filetype]["properties"]["include"]["uniqueItems"] = True
    for key in {"map", "unmap"}:
        schemas[filetype]["properties"][key]["type"] = "object"
        schemas[filetype]["properties"][key]["additionalProperties"] = False
        schemas[filetype]["properties"][key]["properties"] = {}
    # Use list not dict to keep order
    anyOf = [
        {
            "type": "string",
            "enum": keys,
        },
        {
            "type": "string",
            "pattern": "<[ACS]-.*>|.|[a-zA-Z]+",
        },
    ]
    for mode in ["normal", "fullscreen", "presentation", "index"]:
        schemas[filetype]["properties"]["unmap"]["properties"][mode] = {
            "type": "array",
            "items": {"uniqueItems": True, "anyOf": anyOf},
        }
        schemas[filetype]["properties"]["map"]["properties"][mode] = {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "key": {"anyOf": anyOf},
                    "shortcut": {"type": "string", "enum": shortcuts},
                    "argument": {"type": "string", "enum": arguments + [None]},
                },
                "uniqueItems": True,
            },
        }

    schemas[filetype]["properties"]["set"]["properties"] = {}
    schemas[filetype]["properties"]["set"]["additionalProperties"] = False
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
                if (
                    schemas[filetype]["properties"]["set"]["properties"]
                    .get(keyword, {})
                    .get("description")
                    is None
                ):
                    description = " ".join(
                        line.strip()
                        for line in token.content.lstrip(": ").splitlines()
                    )
                    schemas[filetype]["properties"]["set"]["properties"][
                        keyword
                    ] = {"description": description}
                    if (
                        description.find("Possible values are ")
                        == description.find("Possible options are ")
                        == -1
                    ):
                        continue
                    schemas[filetype]["properties"]["set"]["properties"][
                        keyword
                    ]["enum"] = [
                        value.split(" ")[0].replace('\\"', "")
                        for value in description.rpartition(
                            "Possible values are "
                        )[2]
                        .rpartition("Possible options are ")[2]
                        .partition(".")[0]
                        .replace(" and ", ", ")
                        .split(", ")
                    ]
                    continue
                for line in token.content.splitlines():
                    if line.find("Value type: ") != -1:
                        _type = (
                            line.strip().partition("Value type: ")[2].lower()
                        )
                        schemas[filetype]["properties"]["set"]["properties"][
                            keyword
                        ]["type"] = {
                            "int": "integer",
                            "float": "number",
                            "bool": "boolean",
                        }.get(
                            _type, _type
                        )
                    elif line.find("Default value: ") != -1:
                        default = line.strip().partition("Default value: ")[2]
                        _type = schemas[filetype]["properties"]["set"][
                            "properties"
                        ][keyword]["type"]
                        if _type == "integer":
                            default = int(default.split(" ")[0])
                        elif _type == "number":
                            default = float(default)
                        elif _type == "boolean":
                            default = default == "true"
                        schemas[filetype]["properties"]["set"]["properties"][
                            keyword
                        ]["default"] = default
                        if isinstance(default, str) and default.startswith(
                            "#"
                        ):
                            schemas[filetype]["properties"]["set"][
                                "properties"
                            ][keyword]["format"] = "color"

    schemas[filetype]["properties"]["set"]["properties"][
        "highlight-transparency"
    ] |= {"minimum": 0, "maximum": 1}

    schemas[filetype]["properties"]["set"]["properties"]["guioptions"][
        "pattern"
    ] = r"[cshv]*"
    schemas[filetype]["properties"]["set"]["properties"]["first-page-column"][
        "pattern"
    ] = r"\d+(:\d+)*"
    schemas[filetype]["properties"]["set"]["properties"][
        "selection-clipboard"
    ]["enum"] = ["clipboard", "primary"]

    return schemas
