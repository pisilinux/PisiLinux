#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"

version = get.srcVERSION().split("_", 1)[1]
WorkDir = "vdrift-%s-%s-%s" % (version[0:4], version[4:6], version[6:])

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name.startswith("SConscript"):
                shelltools.unlink(os.path.join(root, name))


def setup():
    fixperms("data")

def install():
    pisitools.dodir("/usr/share")
    shelltools.copytree("data", "%s/usr/share/vdrift" % get.installDIR())

