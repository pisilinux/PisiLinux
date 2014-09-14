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
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("RANLIB", get.RANLIB())
    shelltools.export("AR", get.AR())

    # enable-debug is bogus, it should stay here
    options = "--with-x \
               --enable-opengl-player \
               --disable-gtk-player \
               --enable-mmx \
               --disable-assertions \
               --disable-static \
               --enable-debug"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --bindir=/emul32/bin \
                     --includedir=/emul32/include \
                     --mandir=/emul32/man \
                     --disable-sdltest \
                     --disable-gtktest"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())



    shelltools.system("rm -rf acinclude/lt*.m4 acinclude/libtool.m4")

    neededfilelist=["NEWS","ChangeLog","AUTHORS"]
    for i in neededfilelist:
         shelltools.touch(i)

    autotools.autoreconf("-fi -Iacinclude")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "README*", "TODO")
