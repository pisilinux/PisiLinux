#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libname = "libexpect.so.%s" % get.srcVERSION()
majorVersion = tuple(get.srcVERSION().split(".")[:2])

def setup():
    #pisitools.dosed("expect.man", "/usr/local/bin", "/usr/bin")
    #pisitools.dosed("expectk.man", "/usr/local/bin", "/usr/bin")

    pisitools.dosed("Makefile.in", "^install: .*", "install: all install-binaries install-doc")
    pisitools.dosed("Makefile.in", "^(SCRIPTS_MANPAGES = .*)$", "_\\1")

    autotools.autoconf()

    shelltools.export("CFLAGS","%s -D_BSD_SOURCE" % get.CFLAGS())
    autotools.configure("--with-tcl=/usr/lib \
                         --with-tclinclude=/usr/include \
                         --without-x \
                         --with-tk=no \
                         --enable-shared")

def build():
    autotools.make("SONAME=%s" % libname)

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.domove("/usr/lib/expect%s/libexpect%s.so" % (get.srcVERSION(), get.srcVERSION()), "/usr/lib/", libname)

    pisitools.rename("/usr/lib/expect%s" % get.srcVERSION(), "expect%s.%s" % majorVersion)

    #pisitools.dosym(libname, "/usr/lib/libexpect.so.%s.%s" % majorVersion)
    pisitools.dosym(libname, "/usr/lib/libexpect%s.so" % get.srcVERSION())
    pisitools.dosym(libname, "/usr/lib/libexpect.so.%s" % majorVersion[0])
    pisitools.dosym(libname, "/usr/lib/libexpect.so")

    pisitools.dodoc("FAQ", "ChangeLog", "NEWS", "README", "HISTORY")
