import os

home = os.path.expanduser("~")


class path:
    local = os.path.join(home, "bin")
    i3status = os.path.join(home, ".i3status.conf")
    i3 = os.path.join(home, ".i3", "config")
    wallpaper = os.path.join(home, "images", "wallpapers")


class color:
    # main = "#4984bb"

    # main = "#f5d04c"
    main = "#c8972e"

    # main = "#6acf50"
    bg = "#000000"
    fg = "#999999"
    smooth = "#333333"
    alert = "#f42e00"


class wallpaper:
    # name = "adventure-time-mars.jpg"
    # name = "akira-outtro.jpg"
    name = "ghost-in-the-shell-city.jpg"
    # name = "mouse-brain-slice.jpg"
    mode = "fill"

font = "Monaco"
