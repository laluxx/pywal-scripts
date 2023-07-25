import re
import os
import subprocess
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

def update_org_colors_wal(filepath, colors):
    with open(os.path.expanduser(filepath), "r") as file:
        lines = file.readlines()

    # Mapping of org-level-* to colors
    color_mapping = {
        'org-level-1': 'color1',
        'org-level-2': 'color2',
        'org-level-3': 'color3',
        'org-level-4': 'color4',
        'org-level-5': 'color5',
        'org-level-6': 'color6',
        'org-level-7': 'color7',
        'org-level-8': 'color8'
    }

    # Search for laluxx/org-colors-wal function and replace color values with new colors
    in_target_func = False
    for i, line in enumerate(lines):
        if "defun laluxx/org-colors-wal" in line:
            in_target_func = True
        if in_target_func and '))' in line:
            in_target_func = False
        if in_target_func:
            for org_level, color in color_mapping.items():
                if org_level in line:
                    lines[i] = re.sub(r'"#.*?"', f'"{colors[color]}"', line)
                    break

    with open(os.path.expanduser(filepath), "w") as file:
        file.writelines(lines)

    # Invoke a shell command to do a doom sync
    # subprocess.run(['doom', 'sync'])

def main():
    path = "~/.cache/wal/colors-kitty.conf"
    org_file = "~/.config/doom/config.org"
    colors = get_colors(path)
    update_org_colors_wal(org_file, colors)

if __name__ == "__main__":
    main()







# WORK ONLY FIRST TIME
# import re
# import os
# import subprocess
# from itertools import cycle
#
# def get_colors(filepath):
#     colors = {}
#     with open(os.path.expanduser(filepath), "r") as file:
#         lines = file.readlines()
#
#         for line in lines:
#             match = re.search(r"(color\d+|foreground|background)\s+([#\da-fA-F]+)", line)
#             if match:
#                 colors[match.group(1)] = match.group(2)
#     return colors
#
# def update_org_colors_wal(filepath, colors):
#     with open(os.path.expanduser(filepath), "r") as file:
#         lines = file.readlines()
#
#     # Create a cycle of the remaining colors, excluding color0
#     remaining_colors = {k: v for k, v in colors.items() if k != "color0"}
#     color_cycle = cycle(list(remaining_colors.values()))
#
#     # Search for laluxx/org-colors-wal function and replace color values with new colors
#     in_target_func = False
#     for i, line in enumerate(lines):
#         if "defun laluxx/org-colors-wal" in line:
#             in_target_func = True
#         if in_target_func and '))' in line:
#             in_target_func = False
#         if in_target_func and "#" in line:
#             lines[i] = re.sub(r'"#.*?"', f'"{next(color_cycle)}"', line)
#
#     with open(os.path.expanduser(filepath), "w") as file:
#         file.writelines(lines)
#
#     # Invoke a shell command to do a doom sync
#     # subprocess.run(['doom', 'sync'])
#
# def main():
#     path = "~/.cache/wal/colors-kitty.conf"
#     org_file = "~/.config/doom/config.org"
#     colors = get_colors(path)
#     update_org_colors_wal(org_file, colors)
#
# if __name__ == "__main__":
#     main()
