#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("build/tibs/compiler/gcc.mak", "^GCC.CFLAGS.release.*$", "GCC.CFLAGS.release = ")
    pisitools.dosed("build/tibs/compiler/gcc.mak", "^GCC.CXXFLAGS = \$.*$", "GCC.CXXFLAGS = $(GCC.CFLAGS)")

    autotools.rawConfigure("--prefix=/%s --mode=release --staticlibs=NO --target=..generic --vectorization=" % get.defaultprefixDIR())
    pisitools.dosed("config.mak", "CONF_DOCDIR=.*", "CONF_DOCDIR=/usr/share/doc/lensfun/")

def install():
    autotools.install("INSTALL_PREFIX=%s V=1" % get.installDIR())

