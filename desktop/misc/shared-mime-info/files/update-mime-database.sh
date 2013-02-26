if [ -x /usr/bin/update-mime-database ]; then
    MIME_DIR=${XDG_DATA_HOME-$HOME/.local/share}/mime
    [ -d "$MIME_DIR" ] && /usr/bin/update-mime-database $MIME_DIR
fi
