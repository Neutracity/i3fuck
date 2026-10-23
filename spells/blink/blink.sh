#!/bin/sh


if [ "$1" != "--daemon" ]; then
  nohup "$0" --daemon "$@" > /dev/null 2>&1 &
  exit 0
fi


while true ; do
  sleep $((1 + $RANDOM % 120))
  xrandr -o 1
  xrandr -o 0
done
