#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():    
    shelltools.cd("build/workspaces/")
    shelltools.export("WX_CONFIG", "/usr/bin/wx-config-2.8 ")
    shelltools.system("./update-workspaces.sh \
                       --enable-atlas \
                       --with-system-enet \
                       --with-system-mozjs24 \
                       --with-system-miniupnpc \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib/0ad \
                       --datadir=/usr/share/0ad/data \
                       JOBS=%s" % get.makeJOBS())

def build():
    shelltools.cd("build/workspaces/gcc")
    autotools.make()

def install():
    pisitools.dodoc("LICENSE.txt","license_dbghelp.txt","license_gpl-2.0.txt","license_lgpl-2.1.txt","README.txt",)
    pisitools.insinto("/usr/share/0ad", "binaries/*")
    pisitools.insinto("/usr/bin/", "binaries/system/pyrogenesis")
    pisitools.insinto("/usr/lib/0ad/", "binaries/system/*.so*")
    pisitools.insinto("/usr/bin/", "build/resources/0ad.sh")
    pisitools.insinto("/usr/share/pixmaps/", "build/resources/0ad.png", "0ad.png")
    pisitools.insinto("/usr/share/applications/", "build/resources/0ad.desktop", "0ad.desktop")