from utils import row, quotes, write_bash
from config import path, color, font


def generate_bash():
    write_bash(path.local, "menu",
               row("dmenu -b",
                   "-p", quotes("$1"),
                   "-fn {}-9".format(font),
                   "-nb", quotes(color.bg),
                   "-nf", quotes(color.fg),
                   "-sb", quotes(color.bg),
                   "-sf", quotes(color.main)))

    write_bash(path.local, "lsws",
               "i3-msg -t get_workspaces |",
               "tr , '\n' |",
               "grep name |",
               "cut -d \\\" -f 4")
