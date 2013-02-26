#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

def setup():
    shelltools.chmod("worldofpadman.run", 0755)

    shelltools.system("./worldofpadman.run \
                       --noexec \
                       --target %s" % get.workDIR())

    shelltools.system("tar -xvf wop-data.tar")
    shelltools.system("tar -xvf readme.tar")

def install():
    pisitools.insinto("/usr/share/WoP/wop", "*.pk*")
    pisitools.insinto("/usr/share/WoP/wop", "*.cfg")

    pisitools.dodoc("README*", "*.txt")
    pisitools.dohtml("readme/*", "readme.html")
