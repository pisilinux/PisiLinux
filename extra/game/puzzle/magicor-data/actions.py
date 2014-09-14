#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

WorkDir = "magicor-%s" % get.srcVERSION().replace("_", "-")
sharedir = "/usr/share/magicor"
NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("data")

def install():
    pisitools.insinto(sharedir, "data/*")

    pisitools.dodir("/usr/share/pixmaps")
    pisitools.dosym("/usr/share/magicor/sprites/sun.png", "/usr/share/pixmaps/magicor.png")

    pythonmodules.fixCompiledPy("/usr/share/magicor")
