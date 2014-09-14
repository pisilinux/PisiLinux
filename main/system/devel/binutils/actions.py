#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
    #shelltools.export("LD_SYMBOLIC_FUNCTIONS", "1")
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')

    autotools.configure('--enable-shared \
                         --build=%s \
                         --enable-threads \
                         --enable-ld=default \
                         --enable-gold \
                         --enable-plugins \
                         --with-pkgversion="Pisi Linux" \
                         --with-bugurl=http://bugs.pisilinux.org/ \
                         %s \
                         --with-pic \
                         --disable-nls \
                         --disable-werror' % (get.HOST(), multilib))
                         #--enable-targets="i386-linux" \

def build():
    autotools.make("configure-host")
    autotools.make()

# check fails because of LD_LIBRARY_PATH
#def check():
#    autotools.make("check -j1")

def install():
    autotools.rawInstall("DESTDIR=%s tooldir=/usr" % get.installDIR())

    # Rebuild libbfd.a and libiberty.a with -fPIC
    #pisitools.remove("/usr/lib/libbfd.a")
    #pisitools.remove("/usr/lib/libiberty.a")
    # pisitools.remove("/usr/include/libiberty.h")

    autotools.make("-C libiberty clean")
    autotools.make('CFLAGS="-fPIC %s" -C libiberty' % get.CFLAGS())

    autotools.make("-C bfd clean")
    autotools.make('CFLAGS="-fPIC %s" -C bfd' % get.CFLAGS())

    pisitools.insinto("/usr/lib", "bfd/libbfd.a")
    pisitools.insinto("/usr/lib", "libiberty/libiberty.a")
    pisitools.insinto("/usr/include", "include/libiberty.h")
    pisitools.insinto("/usr/include", "include/demangle.h")

    # Copy plugin-api.h file to build LLVM with LLVM gold plugin
    pisitools.insinto("/usr/include", "include/plugin-api.h")

    # Prevent programs to link against libbfd and libopcodes dynamically,
    # they are changing far too often
    pisitools.remove("/usr/lib/libopcodes.so")
    pisitools.remove("/usr/lib/libbfd.so")

    # Remove libtool files, which reference the .so libs
    pisitools.remove("/usr/lib/libopcodes.la")
    pisitools.remove("/usr/lib/libbfd.la")

    # Remove unneded man , info
    unneeded_man={"dlltool.1","nlmconv.1","windres.1","windmc.1"}
    for i in unneeded_man:
        pisitools.remove("/usr/share/man/man1/%s" %i)

    pisitools.remove("/usr/share/info/configure.info")
    pisitools.remove("/usr/share/info/standards.info")

