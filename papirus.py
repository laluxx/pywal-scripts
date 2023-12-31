#!/usr/bin/python
import os
import sys
def literal_color(rgb, color_dict):
    min_colours = {}
    for name, hex_val in color_dict.items():
        rd = (int(hex_val[1:3], 16) - rgb[0])  2
        gd = (int(hex_val[3:5], 16) - rgb[1])  2
        bd = (int(hex_val[5:7], 16) - rgb[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    closest_name = min_colours[min(min_colours.keys())]
    return closest_name
color_dict = {
    "blue": "#0000FF",
    "cyan": "#00FFFF",
    "green": "#00FF00",
    "violet": "#FF00FF",
    "yellow": "#FFFF00",
    "orange": "#FFAA00",
    "red": "#FF0000",
    "black": "#000000"
}
colors_kitty_path = os.path.expanduser("~/.cache/wal/colors-kitty.conf")
with open(colors_kittypath) as file:
    for line in file:
        if "color5" in line:
            , color = line.split()
            break
rgb = [int(color[i:i+2], 16) for i in (1, 3, 5)]
close_color_name = literal_color(rgb, color_dict)
command = f"papirus-folders -t ePapirus-Dark -C {close_color_name}"
os.system(command)
sys.exit()
