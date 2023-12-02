r"""Schema
==========
"""
from dataclasses import dataclass
from typing import Literal

from lsprotocol.types import Position, Range
from tree_sitter import Node
from tree_sitter_lsp import UNI
from tree_sitter_lsp.schema import Trie


@dataclass
class ZathurarcTrie(Trie):
    r"""Zathurarc Trie."""

    value: dict[str, "Trie"] | list["Trie"] | str | Literal[0] = 0

    @classmethod
    def from_string_node(cls, node: Node, parent: "Trie | None") -> "Trie":
        r"""From string node.

        :param cls:
        :param node:
        :type node: Node
        :param parent:
        :type parent: Trie | None
        :rtype: "Trie"
        """
        if node.type == "string" and node.children == 3:
            node = node.children[1]
        text = UNI.node2text(node)
        _range = UNI.node2range(node)
        if node.type in {"string", "raw_string"} and node.children != 3:
            text = text.strip("'\"")
            _range.start.character += 1
            _range.end.character -= 1
        return cls(_range, parent, text)

    @classmethod
    def from_node(cls, node: Node, parent: "Trie | None") -> "Trie":
        r"""From node.

        :param node:
        :type node: Node
        :param parent:
        :type parent: Trie | None
        :rtype: "Trie"
        """
        # if node.type == "set_directive":
        #     node = node.children[1]
        #     return cls(UNI.node2range(node), parent, node.children[2])
        if node.type == "file":
            trie = cls(Range(Position(0, 0), Position(1, 0)), parent, {})
            directives = {
                "set_directive",
                "map_directive",
                "unmap_directive",
            }
            for directive in directives:
                _type = directive.split("_")[0]
                trie.value[_type] = cls(  # type: ignore
                    Range(Position(0, 0), Position(1, 0)), trie, {}
                )
            for child in node.children:
                if child.type not in directives:
                    continue
                subtrie: Trie = trie.value[child.type.split("_")[0]]  # type: ignore
                value: dict[str, Trie] = subtrie.value  # type: ignore
                if child.type == "set_directive":
                    value[UNI.node2text(child.children[1])] = cls.from_node(
                        child, subtrie
                    )
                else:
                    mode = "normal"
                    if child.children[1].type == "mode":
                        mode = child.children[1]
                    value[mode] = cls.from_node(child, subtrie)  # type: ignore
            return trie
        raise NotImplementedError(node.type)
