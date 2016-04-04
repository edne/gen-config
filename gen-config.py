#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import i3

from generate_bash import generate_bash
from generate_i3 import generate_i3
from generate_i3bar import generate_i3bar
from wallpaper import set_wallpaper


if __name__ == "__main__":
    generate_bash()
    generate_i3bar()
    generate_i3()
    set_wallpaper()
    i3.command("reload")
