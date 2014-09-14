# Include the current git branch in the prompt

if type __git_ps1 >/dev/null 2>/dev/null; then
  export PS1="$(echo -n "$PS1" | sed "s|\\\W\]|\\\W\$(__git_ps1 \" (%s)\")\]|")"
fi
