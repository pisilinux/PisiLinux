#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

TR_LANG_DIR = "/usr/share/scidavis/translations"

def setup():
    pisitools.dosed("scidavis/scidavis.pro", "-lgsl -lgslcblas -lz", "-lgsl -lgslcblas -lz -lGLU")
    shelltools.system("qmake SCIDOCDIR=/usr/share/doc/scidavis")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    
    #pisitools.domove("/usr/lib64/scidavis/", "/usr/lib/scidavis")
    #pisitools.removeDir("/usr/lib64")

    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/scidavis.png", "/usr/share/pixmaps/scidavis.png")
    pisitools.dodir(TR_LANG_DIR)
    pisitools.insinto(TR_LANG_DIR, "scidavis/translations/*.qm")