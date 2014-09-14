#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

