import re
import os
from itertools import cycle

def get_colors(filepath):
    colors = {}
    with open(os.path.expanduser(filepath), "r") as file:
        lines = file.readlines()

        for line in lines:
            match = re.search(r"(color\d+|foreground|background)\s+([#\da-fA-F]+)", line)
            if match:
                colors[match.group(1)] = match.group(2)
    return colors

def write_xmobar_config(base_config, colors):
    with open(os.path.expanduser(base_config), 'r') as file:
        config = file.read()

    color_cycle = cycle(list(colors.values()))
    config = re.sub(r'(#)[#\da-fA-F]+', lambda match: next(color_cycle), config)

    with open(os.path.expanduser("~/.config/xmobar/wal-xmobarrc"), "w") as file:
        file.write(config)

def write_wal_hs(colors):
    mapping = {
        'colorBack': 'background',
        'colorFore': 'foreground',
        'color01': 'color0',
        'color02': 'color1',
        'color03': 'color2',
        'color04': 'color3',
        'color05': 'color4',
        'color06': 'color5',
        'color07': 'color6',
        'color08': 'color7',
        'color09': 'color8',
        'color10': 'color9',
        'color11': 'color10',
        'color12': 'color11',
        'color13': 'color12',
        'color14': 'color13',
        'color15': 'color14',
        'color16': 'color15'  # Assign 'color15' from `colors-kitty.conf` to 'color16' in Wal.hs
    }

    color_assignments = "\n".join([f"{key}=\"{colors[value]}\"" for key, value in mapping.items()])

    content = f"""
module Colors.Wal where

import XMonad

colorScheme = "wal"

{color_assignments}

colorTrayer :: String
colorTrayer = "--tint 0x{colors['background'].lstrip('#')}"
"""
    with open(os.path.expanduser("~/.config/xmonad/lib/Colors/Wal.hs"), "w") as file:
        file.write(content.strip())

def main():
    path = "~/.cache/wal/colors-kitty.conf"
    base_config = "~/.config/xmobar/dracula-xmobarrc"
    colors = get_colors(path)
    write_xmobar_config(base_config, colors)
    write_wal_hs(colors)

if __name__ == "__main__":
    main()
