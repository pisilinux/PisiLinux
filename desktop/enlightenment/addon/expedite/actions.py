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
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("--disable-static \
                            --libdir=/usr/lib \
                            --prefix=/usr")
        

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    pisitools.insinto("/usr/share/pixmaps/", "data/3d.png", "expedite.png")

    pisitools.dodoc("AUTHORS", "COPYING*")
