#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from sys import argv
import i3

# set $super Mod4
# bindsym Mod1+n exec i3-input -F 'rename workspace to %s' -P 'New name: '

# main_color="#87af5f"
# main_color="#4984bb"
# main_color="#8787af"
# main_color="#859900"
main_color = "#6acf50"


def lines(*args):
    return "\n".join(args)


def indent(*args):
    return lines(*["    " + l for l in args])


def block(block_header, *args):
    return block_header + " {\n" + indent(*args) + "\n}"


def bindsym(sym, *command):
    return "bindsym {} {}".format(sym, " ".join(command))


def bindsym_exec(sym, *command):
    return "bindsym {} exec {}".format(sym, " ".join(command))


def bindsym_mode(sym, mode_name):
    return "bindsym {} mode \"{}\"".format(sym, mode_name)


def mode(mode_name, *args):
    return block("mode \"" + mode_name + "\"", *args)


def gen_workspaces():
    ws_list = ["~", "www", "irc", "music", "pineal",
               "~", "~", "study", "~", "~"]

    return lines("# Workspaces",
                 bindsym("Mod1+Shift+minus", "move scratchpad"),
                 bindsym("Mod1+minus", "scratchpad show"),
                 "",
                 "workspace 0 output VGA1",
                 "",
                 *[lines(bindsym("Mod1+{i}", "workspace {i}:{name}"),
                         bindsym("Mod1+Shift+{i}",
                                 "move container to workspace {i}:{name}"),
                         "")
                   .format(i=i, name=name)
                   for (i, name) in enumerate(ws_list)])


def gen_movement():
    return lines("# Movement",
                 bindsym("Mod1+h", "focus left"),
                 bindsym("Mod1+j", "focus down"),
                 bindsym("Mod1+k", "focus up"),
                 bindsym("Mod1+l", "focus right"),
                 "",
                 bindsym("Mod1+Left", "focus left"),
                 bindsym("Mod1+Down", "focus down"),
                 bindsym("Mod1+Up", "focus up"),
                 bindsym("Mod1+Right", "focus right"),
                 "",
                 bindsym("Mod1+Shift+h", "move left"),
                 bindsym("Mod1+Shift+j", "move down"),
                 bindsym("Mod1+Shift+k", "move up"),
                 bindsym("Mod1+Shift+l", "move right"),
                 "",
                 bindsym("Mod1+Shift+Left", "move left"),
                 bindsym("Mod1+Shift+Down", "move down"),
                 bindsym("Mod1+Shift+Up", "move up"),
                 bindsym("Mod1+Shift+Right", "move right"),
                 "")


def gen_volume():
    return lines("# Volume",
                 bindsym_exec("XF86AudioRaiseVolume",
                              "amixer -q set Master 5%+ unmute"),

                 bindsym_exec("XF86AudioLowerVolume",
                              "amixer -q set Master 5%- unmute"),

                 bindsym_exec("XF86AudioMute",
                              "amixer -q set Master toggle"),

                 bindsym_exec("XF86AudioMicMute",
                              "amixer -q set Capture toggle"),
                 "")


def gen_actions():
    return lines("# Actions",
                 bindsym("Mod1+q", "kill"),
                 bindsym("Mod1+Shift+c", "reload"),
                 bindsym("Mod1+Shift+r", "restart"),
                 bindsym("Mod1+Shift+e", "i3-nagbar -t warning",
                         "-m 'Do you really want to exit i3?'",
                         "-b 'Yes, exit i3' 'i3-msg exit'"),
                 "")


def gen_commads():
    return lines("# Commands",
                 bindsym_exec("Print",
                              "scrot '%Y-%m-%d-%T_$wx$h.png'",
                              "-e 'mv $f ~/images/'"),
                 bindsym("Mod1+Return", "exec sakura"),
                 bindsym_exec("XF86MonBrightnessUp", "luce +20"),
                 bindsym_exec("XF86MonBrightnessDown", "luce -20"),
                 "",
                 bindsym_exec("XF86ScreenSaver", "~/bin/lock"),
                 "",
                 bindsym_exec("Mod1+d",
                              "PATH=$PATH:~/bin",
                              "dmenu_run -nb \"#000000\" -nf \"#666666\"",
                              "-sb \"#000000\" -sf \"" + main_color + "\""),
                 "")


def gen_windowing():
    return lines("# Windowing",
                 bindsym("Mod1+o", "split h"),
                 bindsym("Mod1+v", "split v"),
                 "floating_modifier Mod1",
                 bindsym("Mod1+t", "floating toggle"),
                 bindsym("Mod1+f", "fullscreen toggle"),
                 bindsym("Mod1+s", "layout stacking"),
                 bindsym("Mod1+w", "layout tabbed"),
                 bindsym("Mod1+e", "layout toggle split"),
                 bindsym("Mod1+space", "focus mode_toggle"),
                 bindsym("Mod1+p", "focus parent"),
                 bindsym("Mod1+c", "focus child"),

                 mode("resize",
                      bindsym("h", "resize shrink width  10 px or 10 ppt"),
                      bindsym("j", "resize grow   height 10 px or 10 ppt"),
                      bindsym("k", "resize shrink height 10 px or 10 ppt"),
                      bindsym("l", "resize grow   width  10 px or 10 ppt"),

                      bindsym_mode("Return", "default"),
                      bindsym_mode("Escape", "default"),
                      ""),
                 bindsym_mode("Mod1+r", "resize"),
                 "")


def gen_bar():
    return lines("# Bar",
                 block("bar",
                       "status_command i3status",
                       "output            LVDS1",
                       "status_command    i3status",
                       "position          bottom",
                       "font pango:DejaVu Sans Mono 7.5",
                       "separator_symbol \" · \"",
                       block("colors",
                             "background #000000",
                             "statusline #999999",
                             "separator " + main_color,
                             "focused_workspace  " + main_color +
                             " #000000 " + main_color,
                             "active_workspace   #000000 #000000 #5f676a"
                             "# inactive_workspace #000000 #000000 #666666",
                             "inactive_workspace #000000 #000000 #999999",
                             "urgent_workspace   #f42e00 #000000 #f42e00"
                             )
                       ),
                 "")


def gen_theme():
    return lines("# Theme",
                 "font pango:DejaVu Sans Mono 8",
                 "client.focused" + main_color +
                 " #000000 " + main_color + " #000000",
                 "client.focused_inactive #999999 #000000 #999999 #484e50",
                 "client.unfocused        #222222 #000000 #999999 #292d2e",
                 "client.urgent           #2f343a #900000 #ffffff #f42e00",
                 "client.placeholder      #000000 #0c0c0c #ffffff #000000",

                 "new_window pixel 1",
                 "new_float  pixel 1"
                 "")


def gen_conf():
    config = lines(gen_workspaces(),
                   gen_movement(),
                   gen_volume(),
                   gen_actions(),
                   gen_commads(),
                   gen_windowing(),
                   gen_bar(),
                   gen_theme(),
                   "")

    if argv[1:]:
        file_name = argv[1]
    else:
        file_name = os.path.expanduser("~") + "/.i3/config"

    with open(file_name, "w") as i3file:
        i3file.write(config)


def i3_config():
    gen_conf()
    i3.command("reload")


if __name__ == "__main__":
    i3_config()
