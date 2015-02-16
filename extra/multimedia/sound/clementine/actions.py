#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(" \
                          -DBUILD_WERROR=OFF \
                          -DBUNDLE_PROJECTM_PRESETS=OFF \
                          -DUSE_BUILTIN_TAGLIB=OFF \
                          -DENABLE_BREAKPAD=OFF \
                          -DENABLE_GIO=ON \
                          -DUSE_SYSTEM_QXT=ON \
                          -DUSE_SYSTEM_GMOCK=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ("16","32","64"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "dist/clementine_%s.png" % i, "clementine.png")

    pisitools.insinto("/usr/share/clementine/locale", "src/translations/*.qm")
    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/clementine.png", "/usr/share/pixmaps/clementine.png")

    pisitools.dodoc("Changelog", "COPYING")