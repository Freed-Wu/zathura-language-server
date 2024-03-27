r"""Test utils."""

import os

from zathura_language_server.finders import ImportZathurarcFinder
from zathura_language_server.utils import get_schema, parser


class Test:
    r"""Test."""

    @staticmethod
    def test_get_schema() -> None:
        r"""Test get schema.

        :rtype: None
        """
        assert len(
            get_schema()
            .get("properties", {})
            .get("set", {})
            .get("description", "")
            .splitlines()
        )

    @staticmethod
    def test_ImportZathurarcFinder() -> None:
        with open(
            os.path.join(os.path.dirname(__file__), "zathurarc"), "rb"
        ) as f:
            text = f.read()
        tree = parser.parse(text)
        assert ImportZathurarcFinder().get_document_links("", tree)
