import os
from subprocess import run
from config import path, wallpaper


def set_wallpaper():
    if wallpaper.mode in ["center", "fill", "max", "scale", "tile"]:
        mode_param = "--bg-" + wallpaper.mode
    else:
        return

    full_path = os.path.join(path.wallpaper, wallpaper.name)
    run(["feh", "--image-bg", "black", mode_param, full_path])
