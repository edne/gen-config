import os

home = os.path.expanduser("~")


class path:
    local = os.path.join(home, "bin")
    i3status = os.path.join(home, ".i3status.conf")
    i3 = os.path.join(home, ".i3/config")


class color:
    # main = "#87af5f"
    # main = "#4984bb"
    # main = "#8787af"
    # main = "#859900"
    main = "#6acf50"
    bg = "#000000"
    fg = "#999999"
    smooth = "#333333"
    alert = "#f42e00"

font = "Monaco"
