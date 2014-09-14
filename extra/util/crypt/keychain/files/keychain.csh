# /etc/profile.d/keychain.csh - calling keychain the Fedora way
# read in user's keychain settings or use defaults running keychain

set userhome = `getent passwd $USER | cut -d: -f6`
if ( "$HOME" == "$userhome" && -f "$HOME/.keychainrc" ) then

    eval `grep -v '^[:blank:]*#' $HOME/.keychainrc | \
	sed 's|\([^=]*\)=\([^=]*\)|set \1 = \2|g' | sed 's|$|;|'`

    if (! $?KCHOPTS) then
	set KCHOPTS = "--quiet"
    endif
    if (! $?prompt) then
	set KCHOPTS = ( $KCHOPTS --noask )
    endif
    if (! $?SSHKEYS) then
	set SSHKEYS = `grep -l -e '[DRS]S[AH] PRIVATE KEY' $HOME/.ssh/*`
    endif
    if (! $?GPGKEYS) then
	set GPGKEYS = ""
    endif

    keychain $KCHOPTS $SSHKEYS $GPGKEYS

    set host = `uname -n`
    if (-f $HOME/.keychain/$host-csh) then
	source $HOME/.keychain/$host-csh
    endif
    if (-f $HOME/.keychain/$host-csh-gpg) then
	source $HOME/.keychain/$host-csh-gpg
    endif

endif

