#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "Nexuiz"
datadir = "/usr/share/quake1"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for d in ["Docs", "data"]:
        fixperms(d)

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("data", "%s/%s/nexuiz" % (get.installDIR(), datadir))

    pisitools.dodoc("Docs/*.txt", destDir="nexuiz")
    pisitools.dohtml("Docs/*", destDir="nexuiz")
    # these are gone for now
    # pisitools.dodoc("Docs/server/*")

