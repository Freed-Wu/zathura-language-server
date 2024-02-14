r"""Finders
===========
"""

import os
from dataclasses import dataclass

from lsprotocol.types import DiagnosticSeverity
from tree_sitter_lsp.finders import ErrorFinder, QueryFinder, SchemaFinder
from tree_sitter_zathurarc import language

from .schema import ZathurarcTrie
from .utils import get_schema


@dataclass(init=False)
class ErrorZathurarcFinder(ErrorFinder):
    r"""Error zathurarc finder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: error",
        severity: DiagnosticSeverity = DiagnosticSeverity.Error,
    ) -> None:
        r"""Init.

        :param filetype:
        :type filetype: str
        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        super().__init__(language, message, severity)


@dataclass(init=False)
class ImportZathurarcFinder(QueryFinder):
    r"""ImportZathurarcFinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: error",
        severity: DiagnosticSeverity = DiagnosticSeverity.Information,
    ):
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        """
        with open(
            os.path.join(
                os.path.join(
                    os.path.join(os.path.dirname(__file__), "assets"),
                    "queries",
                ),
                "import.scm",
            )
        ) as f:
            text = f.read()
        query = language.query(text)
        super().__init__(query, message, severity)


@dataclass(init=False)
class ZathurarcFinder(SchemaFinder):
    r"""Zathurarcfinder."""

    def __init__(self) -> None:
        r"""Init.

        :rtype: None
        """
        self.validator = self.schema2validator(get_schema())
        self.cls = ZathurarcTrie


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorZathurarcFinder,
    ZathurarcFinder,
]
