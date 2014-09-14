#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "./"
NoStrip = "/"

datadir = "/usr/share/queen"
datafiles = ["queen.1c"]

def install():
    pisitools.dodir(datadir)

    for f in datafiles:
        shelltools.chmod(f, 0644)
        pisitools.insinto(datadir, f)

    pisitools.dodoc("readme.txt")

