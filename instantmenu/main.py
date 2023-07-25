import os
import re
import subprocess
import sys
import time

def get_xmobar_colors(xmobar_config_path):
    with open(xmobar_config_path, 'r') as f:
        content = f.read()

    fg_color = re.search(r'fgColor\s*=\s*"([^"]*)"', content).group(1)
    bg_color = re.search(r'bgColor\s*=\s*"([^"]*)"', content).group(1)

    template_colors = re.findall(r'color=#([0-9a-fA-F]{6})', content)

    color = next((color for color in template_colors if color != bg_color), None)

    return fg_color, bg_color, color

def run_instantmenu(history_file, prompt, theme_colors, init_text=None, y_coordinate=None):
    path_programs = subprocess.check_output('compgen -c', shell=True).decode().split('\n')

    history = []
    if os.path.isfile(history_file):
        with open(history_file) as f:
            history = f.read().split('\n')

    menu_list = '\n'.join(history[::-1] + list(set(path_programs) - set(history)))

    fg_color, bg_color, color = theme_colors

    cmd = [
        'instantmenu',
        '-sf', bg_color,
        '-sb', fg_color,
        '-nb', bg_color,
        '-nf', fg_color,
        '-l', '8',
        '-p', prompt,
    ]
    if init_text:
        cmd += ['-it', init_text]
    if y_coordinate:
        cmd += ['-y', str(y_coordinate)]

    proc = subprocess.run(cmd, input=menu_list, capture_output=True, text=True)

    return proc.stdout.strip()

def run_selection(selection, terminal_command=None):
    start_time = time.time()
    try:
        if terminal_command:
            subprocess.run([terminal_command, "-e", selection])
        else:
            subprocess.run(selection, shell=True)
        elapsed_time = time.time() - start_time
        return elapsed_time
    except Exception as e:
        print(f"Error running {selection}: {e}")
        return None

def main():
    history_file = os.path.expanduser('~/.cache/instantmenuhist')
    prompt = "RUN "
    terminal_command = None
    init_text = None
    y_coordinate = 24
    xmobar_config_path = os.path.expanduser('~/.config/xmobar/wal-xmobarrc')

    theme_colors = get_xmobar_colors(xmobar_config_path)

    if len(sys.argv) > 1:
        if sys.argv[1] == "terminal":
            history_file = os.path.expanduser('~/.cache/instanttermmenuhist')
            terminal_command = "~/.config/instantos/default/terminal"
        if len(sys.argv) > 2:
            prompt = sys.argv[1]
            init_text = sys.argv[2]

    selection = run_instantmenu(history_file, prompt, theme_colors, init_text, y_coordinate)

    elapsed_time = run_selection(selection, terminal_command)

    if elapsed_time is not None and elapsed_time > 5:
        with open(history_file, 'a') as f:
            f.write(f"{selection}\n")

if __name__ == "__main__":
    main()


# COLOR version


# import os
# import re
# import sys
# import time
# import subprocess
# from colour import Color

# def lighten_color(color, factor=1.2):
#     c = Color(color)
#     c.luminance = min(1, c.luminance * factor)
#     return str(c)

# def get_non_black_colors(xmobar_config_path):
#     with open(xmobar_config_path, 'r') as f:
#         content = f.read()

#     template_str = re.search(r'template\s*=\s*"([^"]*)"', content).group(1)
#     colors = re.findall(r'color=#([0-9a-fA-F]{6})', template_str)

#     non_black_colors = [f"#{color}" for color in colors if color.lower() != "000000"]

#     if len(non_black_colors) < 2:
#         raise ValueError("No non-black color found in xmobar configuration")

#     return non_black_colors[1], lighten_color(non_black_colors[1])

# def run_instantmenu(history_file, prompt, theme_colors, init_text=None, y_coordinate=None):
#     path_programs = subprocess.check_output('compgen -c', shell=True).decode().split('\n')

#     history = []
#     if os.path.isfile(history_file):
#         with open(history_file) as f:
#             history = f.read().split('\n')

#     menu_list = '\n'.join(history[::-1] + list(set(path_programs) - set(history)))

#     sb_color, sf_color = theme_colors

#     cmd = [
#         'instantmenu',
#         '-sf', sf_color,
#         '-sb', sb_color,
#         '-p', prompt,
#     ]
#     if init_text:
#         cmd += ['-it', init_text]
#     if y_coordinate:
#         cmd += ['-y', str(y_coordinate)]

#     proc = subprocess.run(cmd, input=menu_list, capture_output=True, text=True)

#     return proc.stdout.strip()

# def run_selection(selection, terminal_command=None):
#     start_time = time.time()
#     try:
#         if terminal_command:
#             subprocess.run([terminal_command, "-e", selection])
#         else:
#             subprocess.run(selection, shell=True)
#         elapsed_time = time.time() - start_time
#         return elapsed_time
#     except Exception as e:
#         print(f"Error running {selection}: {e}")
#         return None

# def main():
#     history_file = os.path.expanduser('~/.cache/instantmenuhist')
#     prompt = "xos"
#     terminal_command = None
#     init_text = None
#     y_coordinate = 24
#     xmobar_config_path = os.path.expanduser('~/.config/xmobar/wal-xmobarrc')

#     theme_colors = get_non_black_colors(xmobar_config_path)

#     if len(sys.argv) > 1:
#         if sys.argv[1] == "terminal":
#             history_file = os.path.expanduser('~/.cache/instanttermmenuhist')
#             terminal_command = "~/.config/instantos/default/terminal"
#         if len(sys.argv) > 2:
#             prompt = sys.argv[1]
#             init_text = sys.argv[2]

#     selection = run_instantmenu(history_file, prompt, theme_colors, init_text, y_coordinate)

#     elapsed_time = run_selection(selection, terminal_command)

#     if elapsed_time is not None and elapsed_time > 5:
#         with open(history_file, 'a') as f:
#             f.write(f"{selection}\n")

# if __name__ == "__main__":
#     main()
