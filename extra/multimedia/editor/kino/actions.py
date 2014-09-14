#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    pisitools.dosed("configure", 'LIBS="-lXext', 'LIBS="-lXext -lX11 -lavcodec -lavutil')
    pisitools.dosed("src/Makefile.in", r"\$\(LIBQUICKTIME_LIBS\) \\", r" \\")
    pisitools.dosed("src/Makefile.in", r"(^\s*\$\(SRC_LIBS\))", r"\1 $(LIBQUICKTIME_LIBS)")
    pisitools.dosed("src/filehandler.h", r"^#include <quicktime\.h>", '#include <lqt/quicktime.h>')

    autotools.configure('--disable-debug \
                         --disable-dependency-tracking \
                         --enable-quicktime \
                         --disable-local-ffmpeg')
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*", "BUGS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "TODO")
