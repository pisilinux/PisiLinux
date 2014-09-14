#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

LIBDIR = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
    autotools.rawConfigure("--libdir=%s \
                            --includedir=/usr/include \
                            --prefix=/usr \
                           " % LIBDIR)

def build():
    autotools.make()

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("%s/*.a" % LIBDIR)

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
