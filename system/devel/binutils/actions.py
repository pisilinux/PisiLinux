#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# linker = "gold"
linker = "ld"
multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""

# WorkDir = "binutils-2.20.51"

def setup():
    # Build binutils with LD_SYMBOLIC_FUNCTIONS=1 and reduce PLT relocations in libfd.so by 84%.
    shelltools.export("LD_SYMBOLIC_FUNCTIONS", "1")

    autotools.configure('--enable-shared \
                         --build=%s \
                         --enable-gold \
                         --enable-plugins \
                         --enable-threads \
                         --with-default-linker=%s \
                         --with-pkgversion="Pardus Linux" \
                         --with-bugurl=http://bugs.pardus.org.tr/ \
                         --with-separate-debug-dir=/usr/lib/debug \
                         %s \
                         --disable-nls \
                         --disable-werror' % (get.HOST(), linker, multilib))
                         # --with-pic \
                         #--enable-targets="i386-linux" \

def build():
    autotools.make("all")
    autotools.make("info")

# check fails because of LD_LIBRARY_PATH
#def check():
#    autotools.make("check -j1")

def install():
    autotools.rawInstall("DESTDIR=%s tooldir=/usr" % get.installDIR())

    # Rebuild libbfd.a and libiberty.a with -fPIC
    pisitools.remove("/usr/lib/libbfd.a")
    pisitools.remove("/usr/lib/libiberty.a")
    # pisitools.remove("/usr/include/libiberty.h")

    autotools.make("-C libiberty clean")
    autotools.make('CFLAGS="-fPIC %s" -C libiberty' % get.CFLAGS())

    autotools.make("-C bfd clean")
    autotools.make('CFLAGS="-fPIC %s" -C bfd' % get.CFLAGS())

    pisitools.insinto("/usr/lib", "bfd/libbfd.a")
    pisitools.insinto("/usr/lib", "libiberty/libiberty.a")
    pisitools.insinto("/usr/include", "include/libiberty.h")

    # Copy plugin-api.h file to build LLVM with LLVM gold plugin
    pisitools.insinto("/usr/include", "include/plugin-api.h")

    # Prevent programs to link against libbfd and libopcodes dynamically,
    # they are changing far too often
    pisitools.remove("/usr/lib/libopcodes.so")
    pisitools.remove("/usr/lib/libbfd.so")

    # Remove libtool files, which reference the .so libs
    pisitools.remove("/usr/lib/libopcodes.la")
    pisitools.remove("/usr/lib/libbfd.la")

