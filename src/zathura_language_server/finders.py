r"""Finders
===========
"""

from dataclasses import dataclass

from lsp_tree_sitter.finders import ErrorFinder, QueryFinder, SchemaFinder
from lsprotocol.types import DiagnosticSeverity

from .schema import ZathurarcTrie
from .utils import get_query, get_schema


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
        super().__init__(get_query("import"), message, severity)


@dataclass(init=False)
class ZathurarcFinder(SchemaFinder):
    r"""Zathurarcfinder."""

    def __init__(self) -> None:
        r"""Init.

        :rtype: None
        """
        super().__init__(get_schema(), ZathurarcTrie)


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorFinder,
    ZathurarcFinder,
]
