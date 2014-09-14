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

def fixPerms(datadir):
    # Permissions, permissions, permissions
    for root, dirs, files in os.walk(datadir):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    pisitools.dosed("Makefile", "-O2", get.CFLAGS())
    pisitools.dosed("Makefile", "^MAPC_TARG := mapc", "MAPC_TARG := neverball-mapc")
    # causes sandbox violations
    pisitools.dosed("po/Makefile", "LOCALEDIR", "LLOCALEDIR")

    shelltools.chmod("dist/*.png", 0644)

def build():
    shelltools.export("LINGUAS", "")
    autotools.make("ENABLE_NLS=1 \
                    LOCALEDIR=/usr/share/locale \
                    DATADIR=/usr/share/neverball")

def install():
    for i in ["data", "locale"]:
        fixPerms(i)

    shelltools.copy("dist/mapc.1", "dist/neverball-mapc.6")

    for i in ["neverball", "neverball-mapc", "neverputt"]:
        pisitools.dobin(i)
        pisitools.doman("dist/%s.6" % i)
        if not "mapc" in i:
            pisitools.insinto("/usr/share/pixmaps", "dist/%s_512.png" % i, "%s.png" % i)

    pisitools.insinto("/usr/share", "data", "neverball")
    pisitools.insinto("/usr/share/", "locale")

    pisitools.dodoc("CHANGES", "README")

