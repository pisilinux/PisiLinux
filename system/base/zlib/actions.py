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

def setup():
    options = "--libdir=/usr/lib \
               --includedir=/usr/include \
               --prefix=/usr"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.rawConfigure(options)

def build():
    autotools.make()

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib*/*.a")

    if get.buildTYPE():
        return

    # Copy zlib to /lib
    pisitools.domove("/usr/lib/libz*", "/lib")

    # Create symlinks in /usr/lib
    pisitools.dosym("/lib/libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.%s" % get.srcVERSION())
    pisitools.dosym("libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.1")
    pisitools.dosym("libz.so.1", "/usr/lib/libz.so")

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "doc/*", "examples/*")


if get.buildTYPE() == "minizip":
    minizip_dir = "contrib/minizip"

    def setup():
        shelltools.cd(minizip_dir)
        shelltools.makedirs("m4")

        autotools.autoreconf("-vif")
        # Don't create unnecessary empty /usr/bin
        pisitools.dosed("Makefile.in", "install-exec-am: install-binPROGRAMS install-libLTLIBRARIES", "install-exec-am: install-libLTLIBRARIES")
        autotools.configure("")

    def build():
        autotools.make("-C %s" % minizip_dir)

    def check():
        pass

    def install():
        autotools.rawInstall("-C %s DESTDIR=%s" % (minizip_dir, get.installDIR()))
