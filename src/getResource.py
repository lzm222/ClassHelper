from platformdirs import user_data_dir
from os import path
from shutil import copytree


def getResourcePath(name: str) -> str:
    dir = user_data_dir("classhelper")
    if not path.exists(dir):
        copytree(path.join(path.dirname(__file__), "..", "assets", "default_resource"), dir)
    return path.join(dir, name)
