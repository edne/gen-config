# -*- coding: utf-8 -*-

from utils import row, quotes, write_file
from utils import i3bar_order, i3bar_block
from config import path, color


def generate_i3bar():
    write_file(path.i3status,
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
                           "color_degraded", quotes(color.fg),
                           "color_good", quotes(color.main),
                           "color_bad", quotes(color.alert),
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
