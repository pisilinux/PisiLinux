#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "--disable-static --disable-silent-rules"

    if get.buildTYPE() == "emul32":
        options += "  --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "libopenjpeg/.libs/libopenjpeg.so*")
        pisitools.insinto("/usr/lib32/pkgconfig", "libopenjpeg1.pc")
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("openjpeg-1.5/openjpeg.h", "/usr/include/openjpeg.h")

    pisitools.dodoc("README*")
