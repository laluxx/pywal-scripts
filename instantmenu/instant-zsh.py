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

    proc = subprocess.run(['instantmenu', '-b','-sf', bg_color, '-nb', bg_color, '-nf', fg_color, '-l', '0', '-p', 'RUN ','-h', '15',], #  '-sb', bg_color,
                          input=names_str, capture_output=True, text=True)
    selected_command = proc.stdout.strip()

    os.system(f'zsh -ic "{selected_command}"')

if __name__ == '__main__':
    main()
