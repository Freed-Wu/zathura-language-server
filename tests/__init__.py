"""``{docs,tests}/__init__.py``."""
import sys
import os
from os.path import dirname as dirn

__all__ = []

rootpath = dirn(dirn(os.path.abspath(__file__)))
path = os.path.join(rootpath, "rplugin/python3/syntax-test")
sys.path.insert(0, path)
