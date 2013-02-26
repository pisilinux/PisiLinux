#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("Makefile", "^DOC_PATH=.*$", "DOC_PATH=$(PREFIX)/share/doc/smplayer")

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))

    pisitools.copytree("../smplayer-oxygen-air-theme", "%s/usr/share/smplayer/themes/Oxygen-Air" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/blackPanther-Light", "%s/usr/share/smplayer/themes/blackPanther-Light" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/blackPanther-Real", "%s/usr/share/smplayer/themes/blackPanther-Real" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/blackPanther-VistaLike", "%s/usr/share/smplayer/themes/blackPanther-VistaLike" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Gartoon", "%s/usr/share/smplayer/themes/Gartoon" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Gnome", "%s/usr/share/smplayer/themes/Gnome" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Noia", "%s/usr/share/smplayer/themes/Noia" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Nuvola", "%s/usr/share/smplayer/themes/Nuvola" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Oxygen", "%s/usr/share/smplayer/themes/Oxygen" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Oxygen-Refit", "%s/usr/share/smplayer/themes/Oxygen-Refit" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Silk", "%s/usr/share/smplayer/themes/Silk" % get.installDIR())
    pisitools.copytree("../smplayer-themes-20120919/Tango", "%s/usr/share/smplayer/themes/Tango" % get.installDIR())
