#!/usr/bin/python

import os
import os.path

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R root:cron /var/spool/cron")
    os.system("/bin/chmod -R 01730 /var/spool/cron")

    os.system("/bin/chmod 0755 /etc/conf.d")

    os.system("/bin/chmod 0644 /etc/pam.d/cron")

    os.system("/bin/chown root:wheel /usr/sbin/cron")
    os.system("/bin/chmod 0750 /usr/sbin/cron")

    os.system("/bin/chown root:cron /usr/bin/crontab")
    os.system("/bin/chmod 02755 /usr/bin/crontab")

    crontabs = "/var/spool/cron/crontabs"
    for user in os.listdir(crontabs):
        os.system("/bin/chown %s:cron %s" % (user, os.path.join(crontabs, user)))
        os.system("/bin/chmod 0600 %s" % os.path.join(crontabs, user))
