#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "funnyboat"
NoStrip = "/"

datadir = "/usr/share/funnyboat"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    fixperms(get.workDIR())

    pisitools.dodir(datadir)

    shelltools.copytree("data", "%s/%s/" % (get.installDIR(), datadir))
    shelltools.copy("*.py", "%s/%s/" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/pixmaps", "data/kuvake.png", "funnyboat.png")
    pisitools.dodoc("*.txt")
