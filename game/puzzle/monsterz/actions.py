#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"
datadir = "/usr/share/monsterz"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    shelltools.chmod("monsterz.py", 0755)
    shelltools.move("monsterz.py", "monsterz")

def install():
    pisitools.dobin("monsterz")
    pisitools.dodir(datadir)

    for d in ["graphics", "sound"]:
        fixperms(d)
        shelltools.copytree(d, "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("AUTHORS", "README", "TODO")

