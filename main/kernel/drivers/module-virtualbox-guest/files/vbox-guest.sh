#!/bin/sh

. /etc/conf.d/virtualbox-guest

case $ACTION in
    add)
        if [ "x${LOAD_VBOXSF_MODULE-true}" == "xtrue" ]; then
            /sbin/modprobe -s vboxsf
        fi
        if [ -x /usr/sbin/VBoxService ]; then
            /usr/sbin/VBoxService $VBOXSERVICE_OPTS
        fi
        ;;

    remove)
        ;;

    *)
        exit 1
        ;;
esac
