#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import argv
# import i3


def write_conf():
    ws_list = ["~", "www", "irc", "music", "pineal", "~", "~", "study", "~", "~"]
    workspaces = "\n".join(["""
bindsym $mod+{i} workspace {i}:{name}
bindsym $mod+Shift+{i} move container to workspace {i}:{name}
""".format(i=i, name=name) for (i, name) in enumerate(ws_list)])

    config = """
set $mod Mod1
set $super Mod4
set $altgr Mod5


font pango:DejaVu Sans Mono 8

# Use Mouse+$mod to drag floating windows to their wanted position
floating_modifier $mod


workspace 0 output VGA1
bindsym $mod+n exec i3-input -F 'rename workspace to %s' -P 'New name: '

# start a terminal
bindsym $mod+Return exec sakura

# kill focused window
bindsym $mod+q kill
bindsym $mod+t floating toggle

#bindsym $mod+Control+s exec "scrot '%Y-%m-%d-%T_$wx$h.png' -e 'mv $f ~/images/'"
bindsym Print exec "scrot '%Y-%m-%d-%T_$wx$h.png' -e 'mv $f ~/images/'"


# Pulse Audio controls
#bindsym XF86AudioRaiseVolume exec pactl set-sink-volume 0 +5% #increase sound volume
#bindsym XF86AudioLowerVolume exec pactl set-sink-volume 0 -- -5% #decrease sound volume
#bindsym XF86AudioMute exec pactl set-sink-mute 0 toggle # mute sound
#

# Alsa
bindsym XF86AudioRaiseVolume exec amixer -q set Master 5%+ unmute
bindsym XF86AudioLowerVolume exec amixer -q set Master 5%- unmute
bindsym XF86AudioMute exec amixer -q set Master toggle
bindsym XF86AudioMicMute exec amixer -q set Capture toggle

# Sreen brightness controls
# bindsym XF86MonBrightnessUp exec xbacklight -inc 1  # works?
# bindsym XF86MonBrightnessDown exec xbacklight -dec 1
bindsym XF86MonBrightnessUp exec luce +20
bindsym XF86MonBrightnessDown exec luce -20

#bindsym $altgr+l exec lock
#bindsym ISO_Level3_Shift+l exec lock
bindsym Control+mod1+l exec ~/bin/lock
bindsym XF86ScreenSaver exec ~/bin/lock


# start dmenu (a program launcher)
bindsym $mod+d exec PATH=$PATH:/home/edne/bin dmenu_run -nb "#000000" -nf "#666666" -sb "#000000" -sf "{main_color}"

# change focus
bindsym $mod+h focus left
bindsym $mod+j focus down
bindsym $mod+k focus up
bindsym $mod+l focus right

# alternatively, you can use the cursor keys:
bindsym $mod+Left focus left
bindsym $mod+Down focus down
bindsym $mod+Up focus up
bindsym $mod+Right focus right

# move focused window
bindsym $mod+Shift+h move left
bindsym $mod+Shift+j move down
bindsym $mod+Shift+k move up
bindsym $mod+Shift+l move right

# alternatively, you can use the cursor keys:
bindsym $mod+Shift+Left move left
bindsym $mod+Shift+Down move down
bindsym $mod+Shift+Up move up
bindsym $mod+Shift+Right move right

# split in horizontal orientation
bindsym $mod+o split h

# split in vertical orientation
bindsym $mod+v split v

# enter fullscreen mode for the focused container
bindsym $mod+f fullscreen toggle

# change container layout (stacked, tabbed, toggle split)
bindsym $mod+s layout stacking
bindsym $mod+w layout tabbed
bindsym $mod+e layout toggle split

# toggle tiling / floating
bindsym $mod+Shift+space floating toggle

# change focus between tiling / floating windows
bindsym $mod+space focus mode_toggle

# focus the parent container
bindsym $mod+p focus parent

# focus the child container
bindsym $mod+c focus child

{workspaces}

# bindsym $mod+w exec dmenu_ws -nb "#000000" -nf "#666666" -sb "#000000" -sf "{main_color}"
# bindsym $mod+Shift+w exec dmenu_move_to_ws -nb "#000000" -nf "#666666" -sb "#000000" -sf "{main_color}"


# Make the currently focused window a scratchpad
bindsym $mod+Shift+minus move scratchpad

# Show the first scratchpad window
bindsym $mod+minus scratchpad show

# Show the sup-mail scratchpad window, if any.
#bindsym mod4+s [title="^Sup ::"] scratchpad show


# reload the configuration file
bindsym $mod+Shift+c reload
# restart i3 inplace (preserves your layout/session, can be used to upgrade i3)
bindsym $mod+Shift+r restart
bindsym $mod+Shift+e exec "i3-nagbar -t warning -m 'Do you really want to exit i3?' -b 'Yes, exit i3' 'i3-msg exit'"

mode "resize" {{
        bindsym h resize shrink width  10 px or 10 ppt
        bindsym j resize grow   height 10 px or 10 ppt
        bindsym k resize shrink height 10 px or 10 ppt
        bindsym l resize grow   width  10 px or 10 ppt

        bindsym Return mode "default"
        bindsym Escape mode "default"
}}

bindsym $mod+r mode "resize"

# Start i3bar to display a workspace bar (plus the system information i3status
# finds out, if available)
bar {{
    status_command i3status

    output            LVDS1
    status_command    i3status
    position          bottom

    font pango:DejaVu Sans Mono 7.5

    separator_symbol " · "

    colors {{
            background #000000
            statusline #999999
            separator {main_color}

            focused_workspace  {main_color} #000000 {main_color}
            active_workspace   #000000 #000000 #5f676a
            # inactive_workspace #000000 #000000 #666666
            inactive_workspace #000000 #000000 #999999
            urgent_workspace   #f42e00 #000000 #f42e00
        }}

}}


client.focused          {main_color} #000000 {main_color} #000000
client.focused_inactive #999999 #000000 #999999 #484e50
client.unfocused        #222222 #000000 #999999 #292d2e
client.urgent           #2f343a #900000 #ffffff #f42e00
client.placeholder      #000000 #0c0c0c #ffffff #000000

new_window pixel 1
new_float  pixel 1
    """.format(workspaces=workspaces,
               main_color="#6acf50")
    # main_color="#87af5f")
    # main_color="#4984bb")
    # main_color="#8787af")
    # main_color="#859900")

    if argv[1:]:
        with open(argv[1], "w") as i3file:
            i3file.write(config)


def i3_config():
    write_conf()
    # i3.command("reload")


if __name__ == "__main__":
    i3_config()
