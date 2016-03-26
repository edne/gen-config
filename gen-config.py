#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import stat
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
    return lines("# Workspaces",
                 bindsym_exec("Mod1+Control+l", "i3-msg workspace next"),
                 bindsym_exec("Mod1+Control+h", "i3-msg workspace prev"),

                 bindsym_exec("Mod1+Shift+Control+l",
                              "i3-msg move container to workspace next"),

                 bindsym_exec("Mod1+Shift+Control+h",
                              "i3-msg move container to workspace prev"),

                 bindsym_exec("Mod1+Control+j",
                              "i3-msg workspace back_and_forth"),

                 bindsym_exec("Mod1+Shift+Control+j",
                              "i3-msg move container to workspace"
                              "back_and_forth"),

                 bindsym("Mod1+Control+k", "scratchpad show"),
                 bindsym("Mod1+Shift+Contrl+k", "move scratchpad"),

                 bindsym_exec("Mod1+space",
                              "i3-msg workspace $(lsws | menu)"),

                 bindsym_exec("Mod1+Shift+space",
                              "i3-msg move container to workspace",
                              "$(lsws | menu →)"),

                 "workspace 0 output VGA1",
                 "")


def gen_movement():
    return lines("# Movement",
                 bindsym("Mod1+h", "focus left"),
                 bindsym("Mod1+j", "focus down"),
                 bindsym("Mod1+k", "focus up"),
                 bindsym("Mod1+l", "focus right"),
                 "",
                 bindsym("Mod1+Shift+h", "move left"),
                 bindsym("Mod1+Shift+j", "move down"),
                 bindsym("Mod1+Shift+k", "move up"),
                 bindsym("Mod1+Shift+l", "move right"),
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
                              "dmenu_path | menu \"\" | zsh &"),

                 bindsym_exec("Mod1+semicolon",
                              "PATH=$PATH:~/bin",
                              "stest -flx ~/bin | menu \"\" | zsh &"),
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

home = os.path.expanduser("~")
local_path = home + "/bin"


def gen_bash(name, *code):
    file_name = os.path.join(local_path, name)

    code = lines(*["#!/bin/bash"] + list(code) + [""])

    with open(file_name, "w") as f:
        f.write(code)

    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)


def generate():
    dmenu_colors = ("-nb \"#000000\" -nf \"#666666\" -sb \"#000000\" -sf \"" +
                    main_color +
                    "\"")

    gen_bash("menu", "dmenu -p \"$1\" -b {}".format(dmenu_colors))
    gen_bash("lsws", "i3-msg -t get_workspaces |",
                     "tr , '\n' |",
                     "grep name |",
                     "cut -d \\\" -f 4")

    i3_config = lines(gen_workspaces(),
                      gen_movement(),
                      gen_volume(),
                      gen_actions(),
                      gen_commads(),
                      gen_windowing(),
                      gen_bar(),
                      gen_theme(),
                      "")

    i3_config_file = home + "/.i3/config"
    with open(i3_config_file, "w") as f:
        f.write(i3_config)

    i3.command("reload")


if __name__ == "__main__":
    generate()
