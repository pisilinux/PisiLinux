#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile", "^DOC_PATH=.*$", "DOC_PATH=$(PREFIX)/share/doc/smplayer")

def build():
    autotools.make("PREFIX=/usr QMAKE=/usr/lib/qt5/bin/qmake LRELEASE=/usr/lib/qt5/bin/lrelease")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))

    pisitools.copytree("../smplayer-themes-14.12.0/themes/blackPanther-Light", "%s/usr/share/smplayer/themes/blackPanther-Light" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/blackPanther-Real", "%s/usr/share/smplayer/themes/blackPanther-Real" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/blackPanther-VistaLike", "%s/usr/share/smplayer/themes/blackPanther-VistaLike" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Gnome", "%s/usr/share/smplayer/themes/Faenza" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Gnome", "%s/usr/share/smplayer/themes/Faenza-Darkest" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Gnome", "%s/usr/share/smplayer/themes/Faenza-Silver" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Gartoon", "%s/usr/share/smplayer/themes/Gartoon" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Gnome", "%s/usr/share/smplayer/themes/Gnome" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Monochrome", "%s/usr/share/smplayer/themes/Monochrome" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Noia", "%s/usr/share/smplayer/themes/Noia" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Numix-uTouch", "%s/usr/share/smplayer/themes/Numix-remix" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Numix-uTouch", "%s/usr/share/smplayer/themes/Numix-uTouch" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Nuvola", "%s/usr/share/smplayer/themes/Nuvola" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Oxygen", "%s/usr/share/smplayer/themes/Oxygen" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Oxygen-Air", "%s/usr/share/smplayer/themes/Oxygen-Air" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Oxygen-Air", "%s/usr/share/smplayer/themes/Oxygen-KDE" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Oxygen-Refit", "%s/usr/share/smplayer/themes/Oxygen-Refit" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Silk", "%s/usr/share/smplayer/themes/Silk" % get.installDIR())
    pisitools.copytree("../smplayer-themes-14.12.0/themes/Tango", "%s/usr/share/smplayer/themes/Tango" % get.installDIR())
