#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "redeclipse"

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.dobin("src/reclient")
    pisitools.dobin("src/reserver")

    pisitools.dobin("redeclipse.sh")
    pisitools.rename("/usr/bin/redeclipse.sh", "redeclipse")

    pisitools.insinto("/usr/share/redeclipse", "data/*")

    pisitools.dodoc("readme.txt")
