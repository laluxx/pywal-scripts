# COLORS GOOD
# POSITION GOOD
# TODO alias are not found 
# be smaller 
# vim navigation maube
# atuocompletition inside instantmenu
# keybind for instantmenu inside xmonad
import re
import os
import subprocess

def get_functions_and_aliases(zshrc_path):
    with open(zshrc_path, 'r') as f:
        content = f.read()

    functions = re.findall(r'function\s+(\w+)|(\w+)\s*\(\)', content)

    functions = [name for tuple in functions for name in tuple if name]

    aliases = re.findall(r'^alias\s+(\w+)=', content, re.MULTILINE)

    return functions + aliases

def get_xmobar_colors(xmobar_config_path):
    with open(xmobar_config_path, 'r') as f:
        content = f.read()

    fg_color = re.search(r'fgColor\s*=\s*"([^"]*)"', content).group(1)
    bg_color = re.search(r'bgColor\s*=\s*"([^"]*)"', content).group(1)

    return fg_color, bg_color

def main():
    zshrc_path = os.path.expanduser('~/.config/zsh/.zshrc')
    xmobar_config_path = os.path.expanduser('~/.config/xmobar/wal-xmobarrc')

    names = get_functions_and_aliases(zshrc_path)

    names_str = '\n'.join(names)

    fg_color, bg_color = get_xmobar_colors(xmobar_config_path)

    proc = subprocess.run(['instantmenu', '-sf', fg_color, '-sb', bg_color, '-nb', bg_color, '-nf', fg_color],
                          input=names_str, capture_output=True, text=True)
    selected_command = proc.stdout.strip()

    os.system(f'zsh -ic "{selected_command}"')

if __name__ == '__main__':
    main()


# GOOD colors
# BAD position
# import re
# import os
# import subprocess
#
# def get_functions_and_aliases(zshrc_path):
#     with open(zshrc_path, 'r') as f:
#         content = f.read()
#
#     functions = re.findall(r'function\s+(\w+)|(\w+)\s*\(\)', content)
#
#     functions = [name for tuple in functions for name in tuple if name]
#
#     aliases = re.findall(r'^alias\s+(\w+)=', content, re.MULTILINE)
#
#     return functions + aliases
#
# def get_xmobar_colors(xmobar_config_path):
#     with open(xmobar_config_path, 'r') as f:
#         content = f.read()
#
#     # Extract the foreground and background colors from the xmobar config file.
#     fg_color = re.search(r'fgColor\s*=\s*"([^"]*)"', content).group(1)
#     bg_color = re.search(r'bgColor\s*=\s*"([^"]*)"', content).group(1)
#
#     return fg_color, bg_color
#
# def main():
#     # Path to your .zshrc and xmobar config files.
#     zshrc_path = os.path.expanduser('~/.config/zsh/.zshrc')
#     xmobar_config_path = os.path.expanduser('~/.config/xmobar/wal-xmobarrc')
#
#     # Get all function and alias names.
#     names = get_functions_and_aliases(zshrc_path)
#
#     # Format them into a string, with each name on a separate line.
#     names_str = '\n'.join(names)
#
#     # Get the xmobar colors.
#     fg_color, bg_color = get_xmobar_colors(xmobar_config_path)
#
#     # Calculate menu dimensions.
#     screen_width = os.popen('xdpyinfo | awk \'/dimensions/{print $2}\' | cut -d"x" -f1').read().strip()
#     menu_width = str(int(int(screen_width) * 0.7))
#     menu_height = "30"  # menu height in pixels
#     menu_x = str(int(screen_width) - int(menu_width))
#     menu_y = "0"  # menu y-position (top of the screen)
#
#     # Run instantmenu and capture the selected command.
#     proc = subprocess.run(['instantmenu', '-b', '-c', '-w', menu_width, '-h', menu_height, '-x', menu_x, '-y', menu_y,
#                            '-sf', fg_color, '-sb', bg_color, '-nb', bg_color, '-nf', fg_color],
#                           input=names_str, capture_output=True, text=True)
#     selected_command = proc.stdout.strip()
#
#     # Execute the selected command.
#     os.system(f'zsh -ic "{selected_command}"')
#
# if __name__ == '__main__':
#     main()












# # WORKS :)
# import re
# import os
# import subprocess
#
# def get_functions_and_aliases(zshrc_path):
#     with open(zshrc_path, 'r') as f:
#         content = f.read()
#
#     functions = re.findall(r'function\s+(\w+)|(\w+)\s*\(\)', content)
#
#     functions = [name for tuple in functions for name in tuple if name]
#
#     aliases = re.findall(r'^alias\s+(\w+)=', content, re.MULTILINE)
#
#     return functions + aliases
#
# def main():
#     zshrc_path = os.path.expanduser('~/.config/zsh/.zshrc')
#
#     names = get_functions_and_aliases(zshrc_path)
#
#     names_str = '\n'.join(names)
#
#     proc = subprocess.run(['instantmenu'], input=names_str, capture_output=True, text=True)
#     selected_command = proc.stdout.strip()
#
#     os.system(f'zsh -ic "{selected_command}"')
#
# if __name__ == '__main__':
#     main()
