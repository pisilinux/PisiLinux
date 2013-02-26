#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.unlink("freetennis")
    shelltools.unlink("freetennis.cmi")
    shelltools.unlink("freetennis.cmx")
    shelltools.unlink("freetennis.o")

    autotools.make()

def install():
    pisitools.dobin("freetennis", "/opt/freetennis")

    pisitools.insinto("/opt/freetennis/graphics", "graphics/*")
    pisitools.insinto("/opt/freetennis/sfx", "sfx/*")

    pisitools.dohtml("web-site/*")

    pisitools.dodoc("AUTHORS", "CHANGES*", "COPYING", "TODO*")
