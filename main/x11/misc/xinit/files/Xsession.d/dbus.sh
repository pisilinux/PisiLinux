if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    eval `/usr/bin/dbus-launch --sh-syntax --exit-with-session`
fi
