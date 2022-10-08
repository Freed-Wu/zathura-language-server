"""yaml2json_test."""
from glob import glob
from pathlib import Path

from yaml2json import main  # type: ignore


class Test:
    """Test."""

    def test_syntaxes(self, capsys):
        """test_syntaxes.

        :param capsys:
        """
        for syntax in glob("examples/*.sublime-syntax"):
            main(syntax, "-")
            captured = capsys.readouterr()
            cache = ".".join([syntax.rpartition(".")[0], "json"])
            assert captured.out == Path(cache).read_text()
