# /etc/profile.d/keychain.sh - calling keychain the Fedora way
# read in user's keychain settings or use defaults running keychain

# Don't do anything if we're already done.
[ -n "$KEYCHAIN_DONE" ] && return

userhome=`getent passwd $USER | cut -d: -f6`
if [ "$HOME" = "$userhome" -a -f "$HOME/.keychainrc" ]; then

    . $HOME/.keychainrc

    [ -n "$KCHOPTS" ] || KCHOPTS="--quiet"
    case $- in
	*i*) ;;
	*) KCHOPTS="$KCHOPTS --noask" ;;
    esac
    [ -n "$SSHKEYS" ] || SSHKEYS=`grep -l -e '[DRS]S[AH] PRIVATE KEY' \
							   $HOME/.ssh/*`
    [ -n "$GPGKEYS" ] || GPGKEYS=""

    keychain $KCHOPTS $SSHKEYS $GPGKEYS

    host=`uname -n`
    [ -f $HOME/.keychain/$host-sh ] && \
	. $HOME/.keychain/$host-sh
    [ -f $HOME/.keychain/$host-sh-gpg ] && \
	. $HOME/.keychain/$host-sh-gpg

    unset KCHOPTS SSHKEYS GPGKEYS host

    KEYCHAIN_DONE=1
fi

unset userhome
