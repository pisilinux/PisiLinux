#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("PKG_CONFIG", "/usr/bin/pkg-config")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-spell \
                         --disable-espeak \
                         --disable-festival \
                         --disable-gucharmap")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("usr/share/pixmaps/stardict.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_scan.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_stop.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_normal.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
