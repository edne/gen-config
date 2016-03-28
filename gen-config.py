#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import i3

from utils import row, lines, quotes, write_file, write_bash
from utils import block, bindsym, bindsym_exec, bindsym_mode, mode
from utils import i3bar_order, i3bar_block

home = os.path.expanduser("~")
local_path = os.path.join(home, "bin")

# set $super Mod4
# bindsym Mod1+n exec i3-input -F 'rename workspace to %s' -P 'New name: '

# main_color="#87af5f"
# main_color="#4984bb"
# main_color="#8787af"
# main_color="#859900"

main_color = "#6acf50"
bg_color = "#000000"
fg_color = "#999999"
smooth_color = "#333333"
alert_color = "#f42e00"

font = "Monaco"


def i3conf_workspaces():
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
                 bindsym("Mod1+Shift+Control+k", "move scratchpad"),

                 bindsym_exec("Mod1+space",
                              "i3-msg workspace $(lsws | menu)"),

                 bindsym_exec("Mod1+Shift+space",
                              "i3-msg move container to workspace",
                              "$(lsws | menu →)"),

                 "workspace 0 output VGA1",
                 "")


def i3conf_movement():
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


def i3conf_volume():
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


def i3conf_actions():
    return lines("# Actions",
                 bindsym("Mod1+q", "kill"),
                 bindsym("Mod1+Shift+c", "reload"),
                 bindsym("Mod1+Shift+r", "restart"),
                 bindsym("Mod1+Shift+e", "i3-nagbar -t warning",
                         "-m 'Do you really want to exit i3?'",
                         "-b 'Yes, exit i3' 'i3-msg exit'"),
                 "")


def i3conf_commads():
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
                              "dmenu_path | menu", quotes(""), "| zsh &"),

                 bindsym_exec("Mod1+semicolon",
                              "PATH=$PATH:~/bin",
                              "stest -flx ~/bin |",
                              "menu", quotes(""), "| zsh &"),
                 "")


def i3conf_windowing():
    return lines("# Windowing",
                 bindsym("Mod1+o", "split h"),
                 bindsym("Mod1+v", "split v"),
                 "floating_modifier Mod1",
                 bindsym("Mod1+t", "floating toggle"),
                 bindsym("Mod1+f", "fullscreen toggle"),
                 bindsym("Mod1+s", "layout stacking"),
                 bindsym("Mod1+w", "layout tabbed"),
                 bindsym("Mod1+e", "layout toggle split"),
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


def i3conf_bar():
    return lines("# Bar",
                 block("bar",
                       row("status_command", "i3status"),
                       row("output", "LVDS1"),
                       row("status_command", "i3status"),
                       row("position", "bottom"),
                       "font xft:{} 7".format(font),
                       row("separator_symbol", quotes(" · ")),
                       block("colors",
                             row("background", bg_color),
                             row("statusline", fg_color),
                             row("separator", main_color),
                             row("focused_workspace",
                                 main_color, bg_color, main_color),
                             row("active_workspace",
                                 bg_color, bg_color, "#5f676a"),
                             row("inactive_workspace",
                                 bg_color, bg_color, fg_color),
                             row("urgent_workspace",
                                 alert_color, bg_color, alert_color),
                             "")
                       ),
                 "")


def i3conf_theme():
    return lines("# Theme",
                 "font xft:{} 8".format(font),
                 row("client.focused",
                     main_color, bg_color, main_color, bg_color),
                 row("client.focused_inactive",
                     smooth_color, bg_color, fg_color, bg_color),
                 row("client.unfocused",
                     smooth_color, bg_color, fg_color, bg_color),
                 row("client.urgent",
                     smooth_color, bg_color, fg_color, alert_color),
                 row("client.placeholder",
                     smooth_color, bg_color, fg_color, bg_color),

                 "new_window pixel 1",
                 "new_float  pixel 1"
                 "")


def generate():
    write_bash(local_path, "menu",
               row("dmenu -b",
                   "-p", quotes("$1"),
                   "-fn {}-9".format(font),
                   "-nb", quotes(bg_color),
                   "-nf", quotes(fg_color),
                   "-sb", quotes(bg_color),
                   "-sf", quotes(main_color)))

    write_bash(local_path, "lsws",
               "i3-msg -t get_workspaces |",
               "tr , '\n' |",
               "grep name |",
               "cut -d \\\" -f 4")

    write_file(os.path.join(home, ".i3status.conf"),
               i3bar_order("volume master",
                           "wireless wlp3s0",
                           "ethernet enp0s25",
                           "ethernet tun0",
                           "battery 0",
                           "cpu_temperature 0",
                           "cpu_usage 0",
                           "load",
                           "tztime local"),

               i3bar_block("general",
                           "colors", "true",
                           "color_degraded", quotes(smooth_color),
                           "color_good", quotes(main_color),
                           "color_bad", quotes(alert_color),
                           "output_format", "i3bar",
                           "interval", "1"),

               i3bar_block("wireless wlp3s0",
                           "format_up", quotes(" %quality %essid %ip"),
                           "format_down", quotes("")),

               i3bar_block("ethernet enp0s25",
                           "format_up", quotes("%ip"),
                           "format_down", quotes("")),

               i3bar_block("ethernet tun0",
                           "format_up", quotes("%ip"),
                           "format_down", quotes("")),

               i3bar_block("battery 0",
                           "format", quotes("%status %percentage %remaining"),
                           "format_down", quotes(""),
                           "last_full_capacity", "true",
                           "integer_battery_capacity", "true",
                           "low_threshold", "11",
                           "threshold_type", "percentage",
                           "hide_seconds", "true",
                           "status_chr", quotes(" "),
                           "status_bat", quotes(""),
                           "status_full", quotes(" ")),

               i3bar_block("tztime local",
                           "format", quotes("%A %e.%B %H:%M:%S")),

               i3bar_block("load",
                           "format", quotes(" %1min")),

               i3bar_block("cpu_usage",
                           "format", quotes(" %usage")),

               i3bar_block("cpu_temperature 0",
                           "format", quotes(" %degrees°C")),

               i3bar_block(row("disk", quotes("/")),
                           "format", quotes("%free")),

               i3bar_block(row("disk", quotes("/home")),
                           "format", quotes(" %free")),

               i3bar_block("volume master",
                           "format", quotes(" %volume"),
                           "format_muted", quotes(" --%%"),
                           "device", quotes("default"),
                           "mixer", quotes("Master"),
                           "mixer_idx", "0"))

    write_file(os.path.join(home, ".i3/config"),
               i3conf_workspaces(),
               i3conf_movement(),
               i3conf_volume(),
               i3conf_actions(),
               i3conf_commads(),
               i3conf_windowing(),
               i3conf_bar(),
               i3conf_theme(),
               "")

    i3.command("reload")


if __name__ == "__main__":
    generate()
