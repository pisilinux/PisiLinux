#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ATLAS"

bits = {"i686"  : "32",
        "x86_64": "64"}

cfg = {"bits"  : bits[get.ARCH()],
       "installdir": get.installDIR()
}

def setup():
    #pisitools.dosed("configure", "cc=gcc", "cc=%s" % get.CC())
    #pisitools.dosed("configure", 'cflags="-g.*', "cflags=%s" % get.CFLAGS())

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system("../configure \
                       --prefix=%(installdir)s/usr \
                       --incdir=%(installdir)s/usr/include \
                       --libdir=%(installdir)s/usr/lib \
                       -Si cputhrchk 0 \
                       -Fa alg '-g -Wa,--noexecstack -fPIC' \
                       -D c -DWALL \
                       -b %(bits)s \
                       --with-netlib-lapack=/usr/lib/liblapack.a" % cfg)

    # Fix architecture detection
    if get.ARCH() == "x86_64":
        pisitools.dosed("Make.inc", "ARCH =.*", "ARCH = HAMMER64SSE2")
        pisitools.dosed("Make.inc", "-DATL_SSE3", "")
        pisitools.dosed("Make.inc", "-msse3", "-msse2")
    elif get.ARCH() == "i686":
        pisitools.dosed("Make.inc", "ARCH =.*", "ARCH = PIII32SSE1")
        pisitools.dosed("Make.inc", "-DATL_SSE3 -DATL_SSE2", "")
        pisitools.dosed("Make.inc", "-msse3", "-msse")


def build():
    autotools.make("-C build -j1")
    #autotools.make("-C build/lib shared -j1")

def install():
    pisitools.dodoc("README", "doc/*")

    shelltools.cd("build")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    for i in shelltools.ls("lib/*.so*"):
        pisitools.insinto("/usr/lib/", i)

    pisitools.remove("/usr/lib/*.a")
    #pisitools.remove("/usr/lib/liblapack.so.3")
    #pisitools.remove("/usr/lib/liblapack.so")

