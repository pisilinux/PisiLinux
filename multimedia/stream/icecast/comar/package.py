#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R icecast:icecast /var/log/icecast")
    os.system("/bin/chown -R icecast:icecast /etc/icecast")
    os.system("/bin/chown -R icecast:icecast /run/icecast")
