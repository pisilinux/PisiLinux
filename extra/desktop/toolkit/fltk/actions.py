#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fPIC")
    pisitools.dosed("makeinclude.in", "^(docdir.*)$", r"\1/html")

    autotools.autoconf()

    options = "\
               --enable-gl \
               --enable-shared \
               --enable-threads \
               "

    if get.buildTYPE() == "emul32":

        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")

        options += "--prefix=/usr \
                    --libdir=/usr/lib32 \
                    --with-optim='%s' \
                    " % get.CFLAGS()

    elif get.ARCH() == "x86_64":

        options += "--with-optim='%s' \
                   "  % get.CFLAGS()

    autotools.configure(options)

def build():
    autotools.make()
    autotools.make("-C documentation all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.install("-C documentation")
    autotools.rawInstall("DESTDIR=%s -C fluid" % get.installDIR(), "install-linux")

    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")
