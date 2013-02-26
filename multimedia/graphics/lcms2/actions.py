#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "--disable-dependency-tracking \
               --disable-static \
               --with-jpeg \
               --with-tiff \
               --with-zlib \
               --with-python"
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "src/.libs/liblcms2.so*")
        pisitools.insinto("/usr/lib32/pkgconfig", "lcms2.pc")
        return
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README.1ST")
