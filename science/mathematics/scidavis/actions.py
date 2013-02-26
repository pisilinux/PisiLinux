#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

TR_LANG_DIR = "/usr/share/scidavis/translations"

def setup():
    shelltools.system("qmake SCIDOCDIR=/usr/share/doc/scidavis")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/scidavis.png", "/usr/share/pixmaps/scidavis.png")
    pisitools.dodir(TR_LANG_DIR)
    pisitools.insinto(TR_LANG_DIR, "scidavis/translations/*.qm")
