#!/bin/bash


# TRASPARENT
# Read colors
readarray -t colors < ~/.cache/wal/colors

# Create theme
printf -v theme "BG=%s\nBTN_BG=%s\nBTN_FG=%s\nFG=%s\nGRADIENT=0.0\nHDR_BTN_BG=%s\nHDR_BTN_FG=%s\nHDR_BG=%s\nHDR_FG=%s\nROUNDNESS=4\nSEL_BG=%s\nSEL_FG=%s\nSPACING=3\nTXT_BG=%s\nTXT_FG=%s\nWM_BORDER_FOCUS=%s\nWM_BORDER_UNFOCUS=%s\n" "${colors[0]}" "${colors[1]}" "${colors[2]}" "${colors[3]}" "${colors[4]}" "${colors[5]}" "${colors[6]}" "${colors[7]}" "${colors[8]}" "${colors[1]}" "${colors[2]}" "${colors[3]}" "${colors[4]}" "${colors[5]}"

# Write to a temporary file
temp_file=$(mktemp)
echo -e "$theme" > "$temp_file"

# Change to oomox-gtk-theme directory
cd ~/xos/oomox-gtk-theme

# Execute color change script
./change_color.sh -o wal "$temp_file"

# Remove the temporary file
rm "$temp_file"
