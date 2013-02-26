
SSH_AGENT=/usr/bin/ssh-agent
if [ -x "$SSH_AGENT" -a -z "$SSH_AGENT_PID" ]; then
    STARTUP="$SSH_AGENT $STARTUP"
fi
