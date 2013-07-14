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
    options = "--disable-gtk-doc \
               --with-pcre=system \
               --disable-fam \
               --disable-static \
               --enable-shared \
               --enable-man \
               --enable-systemtap"


    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin \
                     --disable-dtrace"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.autoreconf("-vif")
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "_emul32":
        pisitools.domove("/_emul32/bin/gio-querymodules", "/usr/bin/32/")
        pisitools.removeDir("/_emul32")

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.removeDir("/usr/share/gdb")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
