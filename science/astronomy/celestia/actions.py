#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fsigned-char" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fsigned-char" % get.CXXFLAGS())
    autotools.autoreconf("-fi")
    autotools.configure("--with-gtk \
                         --with-pic \
                         --with-qt \
                         --enable-pch \
                         --disable-rpath \
                         --enable-theora \
                         --enable-cairo \
                         --without-arts \
                         --with-lua")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s MKDIR_P='mkdir -p'" % get.installDIR())
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/kde/data/celestia.desktop")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    #pisitools.insinto("/usr/bin/", "src/celestia/celestia")
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "README", "TRANSLATORS", "locale/COPYING_*")  
    
