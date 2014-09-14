
CK_LAUNCH_SESSION=/usr/bin/ck-launch-session
if [ -x "$CK_LAUNCH_SESSION" -a -z "$XDG_SESSION_COOKIE" ]; then
    STARTUP="$CK_LAUNCH_SESSION $STARTUP"
fi
