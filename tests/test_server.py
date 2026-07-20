import os

from zathura_language_server.server import ZathuraLanguageServer as Server

server = Server("")
file = os.path.join(os.path.dirname(__file__), "zathurarc")


class Test:
    @staticmethod
    def test_check() -> None:
        diagnostics = server.lint(file)[file]
        assert len(diagnostics) > 0

    @staticmethod
    def test_complete() -> None:
        contents = server.lookup("option", "recolor")["recolor"]
        assert len(contents) > 0
