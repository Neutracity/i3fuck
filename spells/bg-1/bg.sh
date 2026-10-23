#!/bin/sh

URL=~/.dotfiles/home/src/wallpaper/nix_white_1.png

feh --bg-scale "$URL"

echo "exec --no-startup-id feh --bg-scale $URL " >> ~/afs/.confs/i3/config
