"""``generate_syntax_test.py``."""
from pathlib import Path

from syntax_test.__main__ import main  # type: ignore

from . import ROOTPATH


class Test:
    """Test."""

    def test_syntaxes(self, capsys):
        """test_syntaxes.

        :param capsys:
        """
        main("-")
        captured = capsys.readouterr()
        cache = Path(ROOTPATH) / "assets" / "json" / "syntax.json"
        assert captured.out == cache.read_text()
