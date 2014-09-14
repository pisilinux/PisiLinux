#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --with-gnu-ld \
                         --enable-nifti \
                         --with-nifti-prefix=/usr")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "etc/xmedcon.png")
    pisitools.dodoc("AUTHORS", "COPYING*", "INSTALL", "NEWS", "README", "REMARKS")
