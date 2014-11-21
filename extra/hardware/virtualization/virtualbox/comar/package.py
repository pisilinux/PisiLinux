#/usr/bin/python
# -*- coding: utf-8 -*-

import os

files = ("VBoxHeadless", "VBoxNetAdpCtl", "VBoxNetDHCP", "VBoxSDL", "VirtualBox")
vboxgroup = "vboxusers"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for _file in files:
        f = "/usr/lib/virtualbox/%s" % _file
        os.system("/bin/chown :%s %s" % (vboxgroup, f))
        os.chmod(f, 04510)
