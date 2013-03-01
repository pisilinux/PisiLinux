#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
