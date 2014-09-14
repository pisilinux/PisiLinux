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

WorkDir = "fillets-ng-data-%s" % get.srcVERSION()
NoStrip = "/"

target = "/usr/share/fish-fillets"
dirs = ["doc", "font", "images", "music", "script", "sound"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for d in dirs:
        fixperms(d)

def install():
    pisitools.dodir(target)
    for d in dirs:
        shelltools.copytree(d, "%s/%s/" % (get.installDIR(), target))

    pisitools.dosym("/usr/share/fish-fillets/images/icon.png", "/usr/share/pixmaps/fillets.png")

    pisitools.dodoc("COPYING")
