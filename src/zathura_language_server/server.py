r"""Server
==========
"""
import re
from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer

from .utils import get_schema


class ZathuraLanguageServer(LanguageServer):
    r"""Zathura language server."""

    def __init__(self, *args: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :rtype: None
        """
        super().__init__(*args)

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            word = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            if not word:
                return None
            result = get_schema()["properties"].get(word[0])
            if not result:
                result = get_schema()["properties"]["set"]["properties"].get(
                    word[0]
                )
                if not result:
                    return None
            return Hover(
                contents=MarkupContent(
                    kind=MarkupKind.Markdown, value=result["description"]
                ),
                range=word[1],
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            word = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            token = "" if word is None else word[0]
            items = [
                CompletionItem(
                    label=x,
                    kind=(
                        CompletionItemKind.Constant
                        if get_schema().get(x, "").startswith(":")
                        else CompletionItemKind.Function
                    ),
                    documentation=MarkupContent(
                        kind=MarkupKind.Markdown,
                        value=get_schema().get(x, {}).get("description", ""),
                    ),
                    insert_text=x,
                )
                for x in get_schema()
                if x.startswith(token)
            ]
            return CompletionList(is_incomplete=False, items=items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        doc = self.workspace.get_document(uri)
        content = doc.source
        line = content.split("\n")[position.line]
        return str(line)

    def _cursor_word(
        self,
        uri: str,
        position: Position,
        include_all: bool = True,
    ) -> tuple[str, Range] | None:
        r"""Cursor word.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :rtype: tuple[str, Range] | None
        """
        pat = r"[a-z_-]+"
        line = self._cursor_line(uri, position)
        cursor = position.character
        for m in re.finditer(pat, line):
            end = m.end() if include_all else cursor
            if m.start() <= cursor <= m.end():
                word = (
                    line[m.start() : end],
                    Range(
                        Position(position.line, m.start()),
                        Position(position.line, end),
                    ),
                )
                return word
        return None
