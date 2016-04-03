import os
import stat
from utils import row, quotes, write_file
from config import path, color, font


def bash(name, *code):
    "Generate an executable bash script"
    file_name = os.path.join(path.local, name)

    code = list(code) + [""]

    write_file(file_name, "#!/bin/bash", *code)

    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)


def generate_bash():
    bash("menu",
         row("dmenu -b",
             "-p", quotes("$1"),
             "-fn {}-9".format(font),
             "-nb", quotes(color.bg),
             "-nf", quotes(color.fg),
             "-sb", quotes(color.bg),
             "-sf", quotes(color.main)))

    bash("lsws",
         "i3-msg -t get_workspaces |",
         "tr , '\n' |",
         "grep name |",
         "cut -d \\\" -f 4")

    bash("lock",
         "killall -SIGUSR1 dunst",
         "i3lock -n -e -f -d -I 5 -c 111111",
         "killall -SIGUSR2 dunst",
         "xset -dpms")

    bash("sprunga",
         "URL=$(cat $1 | curl -F 'sprunge=<-' http://sprunge.us 2> /dev/null)",
         "echo $URL")

    bash("double-screen",
         row("xrandr",
             "--output LVDS1 --primary --mode 1366x768",
             "--pos 0x0 --rotate normal",
             "--output VGA1 --mode 1024x768 --pos 1366x0 --rotate normal",
             "--output HDMI1 --off"))

    bash("single-screen",
         row("xrandr",
             "--output LVDS1 --primary --mode 1366x768",
             "--pos 0x0 --rotate normal",
             "--output VGA1 --off"))

    bash("stacca",
         "single-screen",
         "lock &",
         "systemctl suspend")

    bash("geolocalize",
         "curl http://ip-api.com/line")
