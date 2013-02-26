# /etc/csh.cshrc
#
# This file is sourced by all shells, login and non-login shells.
# Some shells such as scp and rcp don't like any output, so make sure
# this file doesn't display anything, or bad things will happen!
#
# Note that this is the first file the shell reads, hence for login
# shells, the PATH is not yet set!


# Set some variables for interactive shells
if ( $?prompt ) then
	# Find out if we should do colours
	if ( -r /etc/DIR_COLORS ) then
		if ( $?TERM ) then
			set colour = `/bin/egrep "^TERM ${TERM}"'$' /etc/DIR_COLORS`
		endif
	endif

	# Setup colourful stuff if we have color
	set promptchars = "%#"
	if ( $?colour ) then
		if ( "$uid" == "0" ) then
			set prompt = "%{\033[0;1;34m%}(%{\033[0;1;31m%}%m%{\033[0m%}:%{\033[0;1;34m%}%c3%{\033[0;1;34m%}) %{\033[0;1;31m%}%#%{\033[0m%} "
		else
			set prompt = "%{\033[0;1;34m%}(%{\033[0;1;32m%}%m%{\033[0m%}:%{\033[0;1;34m%}%c3%{\033[0;1;34m%}) %{\033[0;1;32m%}%n%{\033[0;1;32m%}%#%{\033[0m%} "
		endif

		# Enable colours for ls, etc.  Prefer ~/.dir_colors
		if ( -f "${HOME}"/.dir_colors ) then
			eval `/usr/bin/dircolors -c "${HOME}"/.dir_colors`
		else if ( -f /etc/DIR_COLORS ) then
			eval `/usr/bin/dircolors -c /etc/DIR_COLORS`
		endif

		alias ls 'ls --color=auto'
		alias grep 'grep --color=auto'
	else
		if ( "$uid" == "0" ) then
			set prompt = "(%m:%c3) %# "
		else
			set prompt = "(%m:%c3) %n%# "
		endif
	endif
	unset colour

	# Change the window title if appropriate
	if ( $?TERM ) then
		switch ( $TERM )
			case xterm*:
			case rxvt:
			case eterm:
			case Eterm:
			case screen:
			case vt100:
				if ( "$uid" == "0" ) then
					set prompt = "%{\033]0;# %m:%~\007%}$prompt"
				else
					set prompt = "%{\033]0;%m:%~\007%}$prompt"
				endif
			breaksw
		endsw
	endif

	# Handle history
	set history = 200
	set histdup = erase

	# Enable editing in EUC encoding for the languages where this make sense
	if ( $?LANG ) then
		switch ( ${LANG:r} )
		case ja*:
			set dspmbyte=euc
			breaksw
		case ko*:
			set dspmbyte=euc
			breaksw
		case zh_TW*:
			set dspmbyte=big5
			breaksw
		default:
			breaksw
		endsw
	endif

	# One can use the "bindkey" facility to redefine the meaning of keys
	# on the keyboard.  While you should set these preferences in your
	# ~/.tcshrc, we include these bindings because many people expect
	# them to be this way.

	# INSERT    : toggles overwrite or insert mode.
	bindkey    ^[[2~  overwrite-mode 
	# DELETE    : delete char at cursor position.
	bindkey    ^[[3~  delete-char
	# HOME      : go to the beginning of the line.
	bindkey    ^[[1~  beginning-of-line
	# END       : go to the end of the line.
	bindkey    ^[[4~  end-of-line
	# PAGE UP   : search in history backwards for line beginning as current.
	bindkey    ^[[5~  history-search-backward
	# PAGE DOWN : search in history forwards for line beginning as current.
	bindkey    ^[[6~  history-search-forward
endif

# Setup a default MAIL variable
if ( -f /var/mail/$USER ) then
    setenv MAIL /var/mail/$USER
    set mail = $MAIL
endif
