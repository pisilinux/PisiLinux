

if [ -x /usr/bin/xhost -a -x /usr/bin/id ]; then
    xhost +si:localuser:`id -un` > /dev/null
fi
xhost +
