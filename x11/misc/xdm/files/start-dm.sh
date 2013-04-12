#!/bin/sh

read_config() {
    FILE=$1
    KEY=$2
    LINE=$(grep "^$KEY=" $FILE)
    VALUE=${LINE#$KEY=}
}

DISPLAY_MANAGER=xdm
XCURSOR_THEME=
PLYMOUTH_TRANSITION=false

test -r /etc/default/xdm && . /etc/default/xdm
test -r /etc/conf.d/xdm && . /etc/conf.d/xdm

DM_PATH=
DESKTOP_FILE=/usr/share/display-managers/$DISPLAY_MANAGER.desktop

if [ -f $DESKTOP_FILE ]; then
    read_config $DESKTOP_FILE Exec
    DM_PATH=$VALUE
    read_config $DESKTOP_FILE X-Pardus-XCursorTheme
    test -n "$VALUE" && XCURSOR_THEME=$VALUE
    read_config $DESKTOP_FILE X-Pardus-PlymouthTransition
    test -n "$VALUE" && PLYMOUTH_TRANSITION=$VALUE
fi

test -x "$DM_PATH" || DM_PATH=/usr/bin/xdm

PATH=/sbin:/usr/sbin:/bin:/usr/bin

test -f /etc/env.d/03locale && . /etc/env.d/03locale

export LC_ALL PATH XCURSOR_THEME

if [ "x$1" = "x--boot" ]; then
    for x in `grep -o -e "xorg=\w*" /proc/cmdline`; do
        case "$x" in
            xorg=safe)
                MESA_LIBGL=/usr/lib/mesa/libGL.so.1.2.0
                if [ "$(readlink /etc/alternatives/libGL)" != "$MESA_LIBGL" ]; then
                    /usr/sbin/alternatives --set libGL /usr/lib/mesa/libGL.so.1.2.0
                    /sbin/ldconfig -X
                fi

                DRIVER=vesa
                test -c /dev/fb0 && DRIVER=fbdev
                export XORGCONFIG=/usr/share/X11/xorg-safe-$DRIVER.conf
                ;;
            xorg=probe)
                test -f /etc/X11/xorg.conf && mv -f /etc/X11/xorg.conf /etc/X11/xorg.conf.$(date +%Y%m%d)
                ;;
        esac
    done
fi

# Trigger events against a locale change. This is needed for
# determining the default keymap.
udevadm trigger --property-match=ID_INPUT_KEYBOARD=1

# Start first boot wizard if needed
if test -f /etc/yali/yali.conf -a -x /usr/bin/start-yali && \
        grep -e "^installation *= *firstboot" /etc/yali/yali.conf; then
    /usr/bin/start-yali

    # First boot wizard removes itself after the last screen. If it
    # still exists at this time, this would mean a reboot or shutdown
    # requested by the user. In this case, we will not start the
    # display manager.
    test -f /usr/bin/start-yali && exit 0
    sleep 1
fi

if [ "$PLYMOUTH_TRANSITION" != "true" ]; then
    test -x /bin/plymouth && /bin/plymouth --ping && /bin/plymouth quit
fi

exec $DM_PATH -nodaemon
