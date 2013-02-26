#!/bin/bash
#
# check if a X session is running and active.
# If not, shut down the system
#
# Copyright (C) 2008 Holger Macht <hmacht@suse.de>
#
# This file is released under the GPLv2.
#

EXEC="/sbin/shutdown -h now"

# iterate over all sessions. If a active X session is found, do nothing
while read A; do
    SESSION=`echo $A | sed 's/\(Session[0-9]*\)://g'`
    [ -z "$SESSION" ] || continue

    SESSION=`echo $A | sed 's/\(Session[0-9]*\):/\1/g'`
    IS_X=`dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit \
    /org/freedesktop/ConsoleKit/$SESSION \
    org.freedesktop.ConsoleKit.Session.GetX11Display`

    # check if this is a X session, if not, go on
    DISP=`echo $IS_X | sed -e 's/^.* string "\(.*\)"/\1/'`
    [ -n "$DISP" ] || continue

    IS_ACTIVE=`dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit \
    /org/freedesktop/ConsoleKit/$SESSION \
    org.freedesktop.ConsoleKit.Session.IsActive`
    IS_ACTIVE=`echo $IS_ACTIVE | sed -e 's/^.* boolean \(.*\)$/\1/'`

    if [ "$IS_ACTIVE" = "true" -a -n "$DISP" ]; then
        # additional check, if none of these two apps are running, go on
        if [ -n "`pidof kded4`" -o -n "`pidof gnome-power-manager`" -o -n "`pidof guidance-power-manager`" -o -n "`pidof kpowersave`" -o -n "`pidof dalston-power-applet`" ]; then
            echo doing nothing...
            exit 0
        fi
    fi
done < <(ck-list-sessions)

logger -s -t acpid "Power Button pressed, executing $EXEC"
$EXEC
