#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #disk aracını mate kontrol merkezine adapte eden satır.
    pisitools.dosed("data/matepalimpsest.desktop.in", "Categories=GTK;System;", "Categories=GTK;Settings;HardwareSettings;")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --disable-static ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "data/icons/48x48/caja-mdu.png")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
