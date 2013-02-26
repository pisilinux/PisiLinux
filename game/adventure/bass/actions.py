#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "bass-cd-%s" % get.srcVERSION()
NoStrip = "/"

datadir = "/usr/share/bass"

def install():
    pisitools.dodir(datadir)

    for f in ["sky.cpt", "sky.dnr", "sky.dsk"]:
        shelltools.chmod(f, 0644)
        pisitools.insinto(datadir, f)

    pisitools.dodoc("readme.txt")

