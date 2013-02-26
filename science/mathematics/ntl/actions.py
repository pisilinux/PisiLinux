#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Filter out -nostdlib from libtool
    shelltools.copy("/usr/bin/libtool", "src")
    pisitools.dosed("src/libtool", "-nostdlib ", "")

    shelltools.cd("src")
    autotools.rawConfigure("PREFIX=/usr \
                            INCLUDEDIR=/usr/include \
                            LIBDIR=/usr/lib \
                            LIBTOOL=./libtool \
                            CC=%s \
                            CXX=%s \
                            CFLAGS=\"%s -fPIC\" \
                            CXXFLAGS=\"%s -fPIC\" \
                            LDFLAGS=\"%s\" \
                            NTL_GMP_LIP=on \
                            SHARED=on" % (get.CC(), get.CXX(),
                                          get.CFLAGS().replace("-O2", "-O1"),
                                          get.CXXFLAGS().replace("-O2", "-O1"),
                                          get.LDFLAGS().replace("-Wl,--hash-style=gnu ", "")))

def build():
    autotools.make("-C src")

#def check():
    #autotools.make("check")

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s \
                          DOCDIR=/usr/share/doc/%s \
                          INCLUDEDIR=/usr/include \
                          LIBDIR=/usr/lib" % (get.installDIR(), get.srcNAME()))

    pisitools.dodoc("../README")
