#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/mail/aliases.db"):
        os.system("/usr/bin/newaliases")

    os.system("/bin/chown root:postdrop /usr/sbin/postdrop")
    os.system("/bin/chown root:postdrop /usr/sbin/postqueue")
    os.system("/bin/chown root:mail /var/spool/mail")
    os.system("/bin/chown postfix:postfix /var/lib/postfix")
    os.system("/bin/chmod 02711 /usr/sbin/postdrop")
    os.system("/bin/chmod 02711 /usr/sbin/postqueue")
    os.system("/bin/chmod 0755 /var/spool/mail")
    os.system("/bin/chmod 0600 /etc/postfix/saslpass")
    os.system("/usr/sbin/postfix check")
