#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    fixperms(".")
    for dirs in ("maps", "fonts", "vehicles", "textures", "events", "sounds", "plugins"):
        shelltools.copytree(dirs, "%s/usr/share/trigger" % get.installDIR())

    pisitools.insinto("/usr/share/trigger", "trigger.config.defs")

    pisitools.dodoc("*.txt")

