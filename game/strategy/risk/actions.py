#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "Domination"
datadir = "/usr/share/risk"

def fixperms(d):
    import os

    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.insinto(datadir, "Domination.jar", "Risk.jar")

    for f in ["help", "maps", "resources" ,"saves"]:
        fixperms(f)
        pisitools.insinto(datadir, f)

    pisitools.dodoc("*.txt")
    pisitools.dohtml("*.htm")
