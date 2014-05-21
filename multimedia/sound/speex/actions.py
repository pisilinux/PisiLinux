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
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

    pisitools.dosed("libspeex/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    options = "--enable-ogg \
               --enable-sse \
               --disable-static"

    if get.buildTYPE() == "emul32":
        # ogg only affects the executables so it's safe to disable for emul32
        options += " --libdir=/usr/lib32 --disable-ogg"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure(options)

    # Remove rpath from speexenc and speexdec
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/speex" % get.installDIR())

    pisitools.dodoc("README")
