# generate the wal.lua file if it doesn't exist

import re
import os
import shutil

# Path to the oxocarbon.lua file
oxocarbon_path = os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/oxocarbon.lua")

# Path to the wal.lua file
wal_path = os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/wal.lua")

# If wal.lua does not exist, create it by copying oxocarbon.lua
if not os.path.exists(wal_path):
    shutil.copyfile(oxocarbon_path, wal_path)

# Read the colors from colors-kitty.conf
colors = {}
with open(os.path.expanduser("~/.cache/wal/colors-kitty.conf")) as f:
    for line in f:
        if re.match(r"color\d", line):
            key, value = line.strip().split()
            colors[key] = value

# Define color mapping based on your colors-kitty.conf and wal.lua
color_mapping = {
    "color0": "black",
    "color1": "red",
    "color2": "green",
    "color3": "yellow",
    "color4": "blue",
    "color5": "purple",
    "color6": "teal",
    "color7": "white",
    "color8": "grey",
    "color9": "baby_pink",
    "color10": "nord_blue",
    "color11": "orange",
    "color12": "light_grey",
    "color13": "grey_fg",
    "color14": "grey_fg2",
    "color15": "lightbg",
}

# Additional mapping for base_16
color_mapping_base_16 = {
    "color0": "base00",
    "color1": "base01",
    "color2": "base02",
    "color3": "base03",
    "color4": "base04",
    "color5": "base05",
    "color6": "base06",
    "color7": "base07",
    "color8": "base08",
    "color9": "base09",
    "color10": "base0A",
    "color11": "base0B",
    "color12": "base0C",
    "color13": "base0D",
    "color14": "base0E",
    "color15": "base0F",
}

# Read the content of wal.lua
with open(wal_path) as f:
    content = f.read()

# Replace the color values for base_30
for key, value in colors.items():
    lua_color = color_mapping.get(key)
    if lua_color:
        pattern = f'{lua_color} = "#[0-9a-fA-F]{{6}}"'
        replacement = f'{lua_color} = "{value}"'
        content = re.sub(pattern, replacement, content)

# Replace the color values for base_16
for key, value in colors.items():
    lua_color = color_mapping_base_16.get(key)
    if lua_color:
        pattern = f'{lua_color} = "#[0-9a-fA-F]{{6}}"'
        replacement = f'{lua_color} = "{value}"'
        content = re.sub(pattern, replacement, content)

# Write the changes back to wal.lua
with open(wal_path, 'w') as f:
    f.write(content)







# DONE but it doesnt create the file
# import re
# import os
#
# # Read the colors from colors-kitty.conf
# colors = {}
# with open(os.path.expanduser("~/.cache/wal/colors-kitty.conf")) as f:
#     for line in f:
#         if re.match(r"color\d", line):
#             key, value = line.strip().split()
#             colors[key] = value
#
# # Define color mapping based on your colors-kitty.conf and wal.lua
# color_mapping = {
#     "color0": "black",
#     "color1": "red",
#     "color2": "green",
#     "color3": "yellow",
#     "color4": "blue",
#     "color5": "purple",
#     "color6": "teal",
#     "color7": "white",
#     "color8": "grey",
#     "color9": "baby_pink",
#     "color10": "nord_blue",
#     "color11": "orange",
#     "color12": "light_grey",
#     "color13": "grey_fg",
#     "color14": "grey_fg2",
#     "color15": "lightbg",
#     # Add more if needed...
# }
#
# # Additional mapping for base_16
# color_mapping_base_16 = {
#     "color0": "base00",
#     "color1": "base01",
#     "color2": "base02",
#     "color3": "base03",
#     "color4": "base04",
#     "color5": "base05",
#     "color6": "base06",
#     "color7": "base07",
#     "color8": "base08",
#     "color9": "base09",
#     "color10": "base0A",
#     "color11": "base0B",
#     "color12": "base0C",
#     "color13": "base0D",
#     "color14": "base0E",
#     "color15": "base0F",
#     # Add more if needed...
# }
#
# # Read the content of wal.lua
# with open(os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/wal.lua")) as f:
#     content = f.read()
#
# # Replace the color values for base_30
# for key, value in colors.items():
#     lua_color = color_mapping.get(key)
#     if lua_color:
#         pattern = f'{lua_color} = "#[0-9a-fA-F]{{6}}"'
#         replacement = f'{lua_color} = "{value}"'
#         content = re.sub(pattern, replacement, content)
#
# # Replace the color values for base_16
# for key, value in colors.items():
#     lua_color = color_mapping_base_16.get(key)
#     if lua_color:
#         pattern = f'{lua_color} = "#[0-9a-fA-F]{{6}}"'
#         replacement = f'{lua_color} = "{value}"'
#         content = re.sub(pattern, replacement, content)
#
# # Write the changes back to wal.lua
# with open(os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/wal.lua"), 'w') as f:
#     f.write(content)




