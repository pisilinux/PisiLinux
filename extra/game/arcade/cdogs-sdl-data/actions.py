#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "cdogs-data-2007-07-06"
NoStrip = "/"

dirs = ["graphics", "missions", "sounds", "music"]
target = "/usr/share/cdogs-sdl"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    fixperms("./")

def install():
    pisitools.dodir(target)
    pisitools.dodir("/usr/share/pixmaps")

    for d in dirs:
        shelltools.copytree(d, "%s/%s" % (get.installDIR(), target))

    pisitools.insinto("/usr/share/pixmaps", "cdogs_icon.png", "cdogs-sdl.png")
