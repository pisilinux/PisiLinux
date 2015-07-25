#!/usr/bin/python

import os, re

OUR_ID = 154
OUR_NAME = "docker"
OUR_DESC = "docker"

logfile = "/var/log/docker.log"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("usr/sbin/groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("usr/sbin/usermod -aG %d %s" % (OUR_ID, OUR_NAME))
        os.system("/bin/touch %s" % logfile)
        os.system("/bin/chown root:docker %s" % logfile)
        os.system("chmod 0644 %s" % logfile)
    except:
        pass

def preRemove():
    try:
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass