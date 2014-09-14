#/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chmod 644 /etc/privoxy/* /etc/privoxy/templates/*")
    os.system("chmod u+x /etc/privoxy/templates")
    os.system("chmod 711 /var/log/privoxy")
    os.system("chmod 744 /usr/sbin/privoxy")

    os.system("chown -R privoxy:privoxy /var/log/privoxy /usr/sbin/privoxy /etc/privoxy")
