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
    options = "--enable-shared --disable-static --disable-silent-rules"

    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")
        
    shelltools.system("./bootstrap.sh")    

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "libopenjpeg/.libs/libopenjpeg.so*")
        pisitools.insinto("/usr/lib32/pkgconfig", "libopenjpeg1.pc")
        pisitools.dosed("%s//usr/lib32/pkgconfig/libopenjpeg1.pc" % get.installDIR(),
                        get.emul32prefixDIR(),
                        get.defaultprefixDIR())
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("openjpeg-1.5/openjpeg.h", "/usr/include/openjpeg.h")

    pisitools.dodoc("README*")
