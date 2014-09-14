[ -e /etc/profile.env ] && . /etc/profile.env

if [ "$EUID" = "0" ] || [ "$USER" = "root" ] ; then
    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${ROOTPATH}"
else
    PATH="/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:${PATH}"
fi
export PATH
unset ROOTPATH
