#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "data"
NoStrip = "/"
datadir = "/usr/share/quake1/nexuiz"

def setup():
    for f in shelltools.ls("./"):
        shelltools.chmod(f, 0644)

def install():
    for f in shelltools.ls("./"):
        pisitools.insinto(datadir, f)
