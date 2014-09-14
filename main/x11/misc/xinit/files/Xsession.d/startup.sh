
DEFAULT_DESKTOP=/etc/default/desktop
USER_XSESSION=$HOME/.xsession
SESSION=$DESKTOP_SESSION
STARTUP=

case $1 in
    failsafe)
        exec -l $SHELL -c "xterm -geometry 80x24-0-0"
        ;;
    custom)
        if [ -x "$USER_XSESSION" ]; then
            STARTUP="$USER_XSESSION"
        fi
        ;;
    default|"")
        test -f $DEFAULT_DESKTOP && . $DEFAULT_DESKTOP

        if [ -n $SESSION ]; then
            desktop_file="/usr/share/xsessions/$SESSION.desktop"
            session_script="/etc/X11/Sessions/$SESSION"

            if [ -f "$desktop_file" ]; then
                STARTUP=`grep "^Exec=" "$desktop_file" | cut -d= -f 2-`
            elif [ -x "$session_script" ]; then
                STARTUP="$session_script"
            fi
        fi
        ;;
    *)
        STARTUP="$1"
        ;;
esac

if [ -z "$STARTUP" ]; then
    # If STARTUP is still empty, try user script first.
    if [ -x "$USER_XSESSION" ]; then
        STARTUP="$USER_XSESSION"
    else
        STARTUP="xsm"
    fi
fi
