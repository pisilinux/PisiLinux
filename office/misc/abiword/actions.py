#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("abiword.desktop", "Icon=abiword", "Icon=/usr/share/pixmaps/abiword.png")
    autotools.autoreconf("-vif")
    
    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-clipart \
                         --enable-templates \
                         --enable-plugins \
                         --enable-statusbar \
                         --with-pic \
                         --disable-collab-backend-service \
                         --disable-collab-backend-tcp")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    pisitools.dosed("config.status", "-lpng15", "")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "abiword.png")
