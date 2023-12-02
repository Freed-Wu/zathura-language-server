r"""Finders
===========
"""
from dataclasses import dataclass

from lsprotocol.types import DiagnosticSeverity
from tree_sitter_lsp.finders import ErrorFinder
from tree_sitter_zathurarc import language


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


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorFinder,
]
