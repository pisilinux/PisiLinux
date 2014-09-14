#/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("mkdir /var/cache/polipo")
    os.system("chmod 0750 /var/cache/polipo")
    os.system("touch /var/log/polipo")
    os.system("chmod 0640 /var/log/polipo")
    os.system("mkdir /run/polipo")
    os.system("chmod 0755 /run/polipo")
    os.system("chown -R polipo:polipo /var/log/polipo /var/cache/polipo /etc/polipo /run/polipo")
