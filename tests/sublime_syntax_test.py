"""``generate_syntax_test.py``."""
from pathlib import Path

from sublime_syntax.scope import main as generate_scope  # type: ignore
from sublime_syntax.syntax import main as generate_syntax  # type: ignore

from . import ROOTPATH


class Test:
    """Test."""

    def test_scope(self, capsys):
        """test_scope.

        :param capsys:
        """
        generate_scope("-")
        captured = capsys.readouterr()
        cache = Path(ROOTPATH) / "assets" / "json" / "scope.json"
        assert captured.out == cache.read_text()

    def test_syntax(self, capsys):
        """test_syntax.

        :param capsys:
        """
        generate_syntax("-")
        captured = capsys.readouterr()
        cache = Path(ROOTPATH) / "assets" / "json" / "syntax.json"
        assert captured.out == cache.read_text()
