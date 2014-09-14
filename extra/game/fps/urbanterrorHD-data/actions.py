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

WorkDir = "UrbanTerror-data/q3ut4"
NoStrip = "/"

datadir = "/usr/share/urbanterrorHD/baseut4"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for files in ["*.pk3", "*.cfg", "mapcycle_example.txt"]:
        pisitools.insinto(datadir, files)

    #for dirs in ["demos", "screenshots"]:
        #shelltools.copytree(dirs, "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("*.doc", "readme42.txt")

    fixperms(get.installDIR())
