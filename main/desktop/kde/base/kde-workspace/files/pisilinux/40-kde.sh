
#kde and kde-safe is changed to kde-plasma and kde-plasma-safe in KDE 4.6
if [ "$SESSION" = "kde" -o "$SESSION" = "kde-safe" -o "$SESSION" = "kde-plasma" -o "$SESSION" = "kde-plasma-safe" -o "$SESSION" = "openbox-kde" ]; then
    kdehome=$HOME/.kde
    test -n "$KDEHOME" && kdehome=`echo "$KDEHOME"|sed "s,^~/,$HOME/,"`

    # see kstartupconfig source for usage
    mkdir -m 700 -p $kdehome/share
    mkdir -m 700 -p $kdehome/share/config
    cat >$kdehome/share/config/startupconfigkeys <<EOF
kcminputrc Mouse cursorTheme 'Oxygen_White'
kcminputrc Mouse cursorSize ''
EOF
    kstartupconfig4
    returncode=$?
    if test $returncode -ne 0; then
        xmessage -geometry 500x100 "kstartupconfig4 does not exist or fails. The error code is $returncode. Check your installation."
        exit 1
    fi
    [ -r $kdehome/share/config/startupconfig ] && . $kdehome/share/config/startupconfig

    # XCursor mouse theme needs to be applied here to work even for kded or ksmserver
    if test -n "$kcminputrc_mouse_cursortheme" -o -n "$kcminputrc_mouse_cursorsize" ; then
        kapplymousetheme "$kcminputrc_mouse_cursortheme" "$kcminputrc_mouse_cursorsize"
        if test $? -eq 10; then
            XCURSOR_THEME=default
            export XCURSOR_THEME
        elif test -n "$kcminputrc_mouse_cursortheme"; then
            XCURSOR_THEME="$kcminputrc_mouse_cursortheme"
            export XCURSOR_THEME
        fi
        if test -n "$kcminputrc_mouse_cursorsize"; then
            XCURSOR_SIZE="$kcminputrc_mouse_cursorsize"
            export XCURSOR_SIZE
        fi
    fi

    if test -z "$XDG_DATA_DIRS"; then
        XDG_DATA_DIRS="${XDG_DATA_DIRS:+$XDG_DATA_DIRS:}/usr/share/kde4:/usr/share:/usr/local/share"
        export XDG_DATA_DIRS
    fi

    KDE_FULL_SESSION=true
    export KDE_FULL_SESSION

    KDE_SESSION_VERSION=4
    export KDE_SESSION_VERSION

    KDE_SESSION_UID=`id -ru`
    export KDE_SESSION_UID

    if test -f /usr/share/kde4/config/gtkrc; then
        GTK2_RC_FILES="${GTK2_RC_FILES:+$GTK2_RC_FILES:}/usr/share/kde4/config/gtkrc"
        export GTK2_RC_FILES

        GTK_RC_FILES=$GTK2_RC_FILES
        export GTK_RC_FILES
    fi
fi
