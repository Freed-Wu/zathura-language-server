r"""Test utils."""

from zathura_language_server.utils import get_schema


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
