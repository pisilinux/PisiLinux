# A little fix so mc exits into it's current working directory
export MC_ENV=/usr/share/mc/bin/mc.sh

for i in $MC_ENV; do
    if [ -x $i ]; then
        . $i
    fi
done

# include this, so also xterm,kterm,gterm,etc will have default bash settings

#if [ "x$SHLVL" != "x1" ]; then # We're not a login shell
#   . /etc/profile
#fi
