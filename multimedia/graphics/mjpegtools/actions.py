#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mjpegtools-2.1.0"

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-vfi")

    pisitools.dosed("configure", "ARCHFLAGS=.*", "ARCHFLAGS=")
    autotools.configure("--with-x \
                         --enable-largefile \
                         --disable-simd-accel \
                         --with-dv-yv12 \
                         --disable-static \
                         --with-libpng \
                         --with-libdv=/usr")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","README*","mjpeg_howto.txt", "TODO")
