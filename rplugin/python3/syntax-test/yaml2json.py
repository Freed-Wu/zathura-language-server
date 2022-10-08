#!/usr/bin/env python
"""Convert *.sublime-syntax to json cache."""
import sys
import json

import yaml


def add_item_to_ret(scope, context, ret):
    """add_item_to_ret.

    :param scope:
    :param context:
    :param ret:
    """
    if scope:
        match = context.get("match", "")
        ret += [{"word": scope, "menu": match}]
        scope = scope.rpartition(".")[0]
        add_item_to_ret(scope, context, ret)


def main(inp: str = "", out: str = ""):
    """Run main function.

    :param inp:
    :type inp: str
    :param out:
    :type out: str
    """
    if inp == "" and out == "":
        inp, out = sys.argv[-2:]
    with open(inp) as f:
        try:
            syntax = yaml.load(f, yaml.CLoader)
        except Exception:
            syntax = yaml.load(f, yaml.Loader)
    contexts = syntax.get("contexts", {})
    ret = []
    for context in sum(contexts.values(), []):
        scopes = context.get("scope", "").split(" ")
        for scope in scopes:
            add_item_to_ret(scope, context, ret)

    if out == "-":
        f = sys.stdout
        json.dump(ret, f)
    else:
        with open(out, "w") as f:
            json.dump(ret, f)


if __name__ == "__main__":
    main()
