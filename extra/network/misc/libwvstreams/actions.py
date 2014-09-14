#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "wvstreams-%s" % get.srcVERSION()

def setup():
    shelltools.export("CXXFLAGS", "%s -DUSE_LOCKDEV=1" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "^LIBS \+=(.*)$", "LIBS +=\\1 -llockdev")
    autotools.configure("--with-dbus \
                         --with-pam \
                         --with-openssl \
                         --without-qt \
                         --without-tcl \
                         --without-valgrind")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/pkgconfig/libwvqt.pc")

    pisitools.removeDir("/usr/lib/valgrind")
    pisitools.removeDir("/usr/share/man")
    pisitools.removeDir("/usr/sbin")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/etc")
    pisitools.removeDir("/var")

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("LICENSE", "README")
