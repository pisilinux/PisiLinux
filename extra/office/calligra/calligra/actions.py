#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

def setup():
    kde4.configure("-DIHAVEPATCHEDQT=1 \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_active=OFF \
                    -DWITH_OCIO=OFF \
                    -DBUILD_cstester=OFF \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DBUILD_mobile=OFF \
                    -DCMAKE_INSTALL_PREFIX=/usr ")

def build():
    kde4.make()

def install():
    kde4.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README", "doc/status.txt")

    pisitools.remove("/usr/share/kde4/apps/color-schemes/KritaDarker.colors")
    pisitools.remove("/usr/share/kde4/apps/color-schemes/Krita50.colors")
    pisitools.remove("/usr/share/kde4/apps/color-schemes/KritaBlender.colors")
    pisitools.remove("/usr/share/kde4/apps/color-schemes/KritaBrighter.colors")
    pisitools.remove("/usr/share/kde4/apps/color-schemes/KritaBright.colors")
    pisitools.remove("/usr/share/kde4/apps/color-schemes/KritaDark.colors")
    
    #for <Icon></Icon>
    pisitools.dopixmaps("braindump/data/icons/hi32-app-braindump.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-braindump.png", "calligra-braindump.png")

    pisitools.dopixmaps("flow/pics/hi32-app-calligraflow.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligraflow.png", "calligra-flow.png")

    pisitools.dopixmaps("karbon/pics/app/hi32-app-calligrakarbon.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligrakarbon.png", "calligra-karbon.png")

    pisitools.dopixmaps("kexi/pics/app/hi32-app-calligrakexi.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligrakexi.png", "calligra-kexi.png")

    pisitools.dopixmaps("plan/pics/hi32-app-calligraplan.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligraplan.png", "calligra-plan.png")

    pisitools.dopixmaps("sheets/data/pics/hi32-app-calligrasheets.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligrasheets.png", "calligra-sheets.png")

    pisitools.dopixmaps("stage/pics/hi32-app-calligrastage.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligrastage.png", "calligra-stage.png")

    pisitools.dopixmaps("words/pics/hi32-app-calligrawords.png")
    pisitools.rename("/usr/share/pixmaps/hi32-app-calligrawords.png", "calligra-words.png")
