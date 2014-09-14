#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ogdi-3.2.0.beta2"

shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))

def setup():
    autotools.configure('--with-zlib \
                         --with-projlib="-L/usr/lib -lproj" \
                         --with-expat \
                         --with-binconfigs')

def build():
    shelltools.export("TARGET", "Linux")
    shelltools.export("CFG", "release")
    autotools.make("-j1")

def install():
    pisitools.dolib_so("bin/Linux/*.so")
    pisitools.dosym("/usr/lib/libogdi.so", "/usr/lib/libogdi.so.3")

    for i in ["gltpd", "ogdi_import", "ogdi_info"]:
        pisitools.dobin("bin/Linux/%s" % i)
    pisitools.dobin("ogdi-config")

    pisitools.insinto("/usr/lib/pkgconfig", "ogdi.pc")

    pisitools.insinto("/usr/include", "ogdi/include/*.h")

    pisitools.dodoc("ChangeLog", "NEWS", "README")
