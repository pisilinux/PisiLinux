#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown ntlmaps:ntlmaps /etc/ntlmaps/server.cfg")
    os.system("/bin/mkdir -m 0770 /var/log/ntlmaps")
    os.system("/bin/chown ntlmaps:ntlmaps /var/log/ntlmaps")
