# command-not-found handle support
if [ -x /usr/bin/command-not-found ]; then
	function command_not_found_handle
	{
		/usr/bin/command-not-found $1
		return $?
	}
fi
