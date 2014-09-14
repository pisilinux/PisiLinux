#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "fgdata"
NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def install():
    pisitools.dodir("/usr/share")
    shelltools.cd("..")
    fixperms(WorkDir)
    shelltools.copytree(WorkDir, "%s/usr/share/flightgear" % get.installDIR())
