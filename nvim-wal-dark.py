# generate the wal-dark.lua file if it doesn't exist
# inside ~/.local/share/nvim/lazy/base46/lua/base46/themes

# DARK VERSION

# TODO: make this actually dark [x]
# meaning the bg is not trasparent


import re
import os
import shutil

# Path to the oxocarbon.lua file
oxocarbon_path = os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/oxocarbon.lua")

# Path to the wal-dark.lua file
wal_path = os.path.expanduser("~/.local/share/nvim/lazy/base46/lua/base46/themes/wal-dark.lua")

# If wal-dark.lua does not exist, create it by copying oxocarbon.lua
if not os.path.exists(wal_path):
    shutil.copyfile(oxocarbon_path, wal_path)

# Read the colors from ~/.cache/wal/colors
colors = []
with open(os.path.expanduser("~/.cache/wal/colors")) as f:
    colors = [line.strip() for line in f]

# Define color mapping based on your colors-kitty.conf and wal-dark.lua
color_mapping = {
    "color0": "black",
    "color1": "red",
    "color2": "green",
    # continue with the rest of your mappings...
}

# Read the content of wal-dark.lua
with open(wal_path) as f:
    content = f.read()

# Replace the color values in wal-dark.lua
for index, color in enumerate(colors):
    lua_color = color_mapping.get(f"color{index}")
    if lua_color:
        pattern = f'{lua_color} = "#[0-9a-fA-F]{{6}}"'
        replacement = f'{lua_color} = "{color}"'
        content = re.sub(pattern, replacement, content)

# Write the changes back to wal-dark.lua
with open(wal_path, 'w') as f:
    f.write(content)
