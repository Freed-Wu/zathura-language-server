"""``generate_syntax_test.py``."""
from pathlib import Path

from sublime_syntax.__main__ import main  # type: ignore

from . import ROOTPATH


class Test:
    """Test."""

    def test_syntax(self, capsys):
        """test_syntax.

        :param capsys:
        """
        main("-")
        captured = capsys.readouterr()
        cache = Path(ROOTPATH) / "assets" / "json" / "sublime-syntax.json"
        assert captured.out == cache.read_text()
