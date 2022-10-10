"""``{docs,tests}/__init__.py``."""
import os
from os.path import dirname as dirn
import sys
from typing import Final

__all__ = ["ROOTPATH"]

ROOTPATH: Final = dirn(dirn(os.path.abspath(__file__)))
path = os.path.join(ROOTPATH, "rplugin/python3")
sys.path.insert(0, path)
