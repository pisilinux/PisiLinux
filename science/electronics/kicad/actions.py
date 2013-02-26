#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s.orig" % (get.srcNAME(), get.srcVERSION().replace("_",".") )
internat = "usr/share/kicad/internat"

shelltools.export("HOME", get.workDIR())

def setup():
    #configure for kicad
    shelltools.cd("kicad")
    cmaketools.configure("-DwxWidgets_USE_STATIC=OFF \
                          -DKICAD_MINIZIP=OFF \
                          -DKICAD_STABLE_VERSION=ON \
                          -DwxWidgets_USE_STATIC=OFF \
                          -DCMAKE_BUILD_TYPE=Release")
    shelltools.cd("..")
    #configure for kicad-library and kicad-docs
    for i in ["kicad-library", "kicad-doc"]:
        shelltools.cd(i)
        cmaketools.configure("-DCMAKE_BUILD_TYPE=Release")
        shelltools.cd("..")


def build():
    for i in ["kicad", "kicad-library"]:
        shelltools.cd(i)
        cmaketools.make()
        shelltools.cd("..")

def install():
    for i in ["kicad", "kicad-library", "kicad-doc"]:
        shelltools.cd(i)
        cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("..")

    pisitools.insinto("/usr/share/pixmaps", "kicad/bitmaps/icon_eeschema.xpm", "eeschema.xpm")
    pisitools.remove("%s/kicad/INSTALL.txt" % get.docDIR())

    shelltools.cd("kicad")
    pisitools.dodoc("AUTHORS.txt", "CHANGELOG*", "COPYRIGHT.txt", "TODO.txt", "version.txt")
    shelltools.cd("..")

    #move locales, wtf is internat directory :S
    for i in shelltools.ls("%s/%s" % (get.installDIR(), internat)):
        pisitools.domove("%s/%s/kicad.mo" % (internat, i), "/usr/share/locale/%s/LC_MESSAGES/" % i )
    pisitools.removeDir(internat)

