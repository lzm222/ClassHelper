import sys
from os import path


def getResourcePath(name: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        workSpace = path.dirname(sys.executable)
    else:
        workSpace = path.dirname(path.dirname(__file__))
    return path.normpath(path.join(workSpace, "resource", name))
