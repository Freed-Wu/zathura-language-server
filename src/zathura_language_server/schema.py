r"""Schema
==========
"""
from dataclasses import dataclass

from lsprotocol.types import Position, Range
from tree_sitter import Node
from tree_sitter_lsp import UNI
from tree_sitter_lsp.schema import Trie


@dataclass
class ZathurarcTrie(Trie):
    r"""Zathurarc Trie."""

    value: dict[str, "Trie"] | list["Trie"] | str | int | float | bool | None

    @classmethod
    def from_node(cls, node: Node, parent: "Trie | None") -> "Trie":
        r"""From node.

        :param node:
        :type node: Node
        :param parent:
        :type parent: Trie | None
        :rtype: "Trie"
        """
        if node.type == "set_directive":
            node = node.children[2]
            _type = node.type
            if _type == "int":
                convert = int
            elif _type == "float":
                convert = float
            elif _type == "bool":
                convert = bool
            else:
                convert = lambda x: x.strip("'\"")
            return cls(
                UNI.node2range(node), parent, convert(UNI.node2text(node))
            )
        if node.type == "map_directive":
            trie = cls(UNI.node2range(node), parent, {})
            value: dict[str, Trie] = trie.value  # type: ignore
            key: Node = node.children[1]
            if key.type == "mode":
                key: Node = key.next_sibling  # type: ignore
            subtrie = value[UNI.node2text(key)] = cls(UNI.node2range(key), trie, {})  # type: ignore
            subvalue: dict[str, Trie] = subtrie.value  # type: ignore

            shortcut: Node = key.next_sibling  # type: ignore
            argument = shortcut.next_sibling
            subvalue["shortcut"] = cls(UNI.node2range(shortcut), trie, UNI.node2text(shortcut))  # type: ignore
            if argument := shortcut.next_sibling:
                subvalue["argument"] = cls(UNI.node2range(argument), trie, UNI.node2text(argument))  # type: ignore
            return trie
        if node.type == "unmap_directive":
            key = node.children[1]
            if key.type == "mode":
                key = key.next_sibling  # type: ignore
            return cls(UNI.node2range(key), parent, UNI.node2text(key))
        if node.type == "file":
            trie = cls(Range(Position(0, 0), Position(1, 0)), parent, {})
            directives = {
                "set_directive",
                "map_directive",
                "unmap_directive",
                "include_directive",
            }
            for directive in directives:
                _type = directive.split("_")[0]
            for child in node.children:
                if child.type not in directives:
                    continue
                _type = child.type.split("_")[0]
                value: dict[str, Trie] = trie.value  # type: ignore
                if _type not in value:
                    trie.value[_type] = cls(  # type: ignore
                        UNI.node2range(child),
                        trie,
                        {} if _type != "include" else [],
                    )
                subtrie: Trie = trie.value[child.type.split("_")[0]]  # type: ignore
                value: dict[str, Trie] | list[Trie] = subtrie.value  # type: ignore
                if child.type == "set_directive":
                    value: dict[str, Trie]
                    value[UNI.node2text(child.children[1])] = cls.from_node(
                        child, subtrie
                    )
                elif child.type == "include_directive":
                    value += [  # type: ignore
                        cls(
                            UNI.node2range(child.children[1]),
                            subtrie,
                            UNI.node2text(child.children[1]),
                        )
                    ]
                else:
                    mode = "normal"
                    if child.children[1].type == "mode":
                        mode = (
                            UNI.node2text(child.children[1])
                            .lstrip("[")
                            .rstrip("]")
                        )
                    if mode not in value:
                        value[mode] = cls(
                            Range(Position(0, 0), Position(1, 0)),
                            subtrie,
                            [],
                        )
                    if child.type == "unmap_directive":
                        value[mode].value += [  # type: ignore
                            cls.from_node(child, value[mode])
                        ]
                    else:
                        value[mode].value += [cls.from_node(child, value[mode])]  # type: ignore
            return trie
        raise NotImplementedError(node.type)
