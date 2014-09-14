#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    for f in ["NEWS", "README", "AUTHORS"]:
        shelltools.touch(f)

    # fix building against automake-1.12
    pisitools.dosed("configure.in", "^AM_C_PROTOTYPES")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-examples \
                         --enable-ctrl \
                         --enable-platform \
                         --enable-freetype \
                         --enable-gpc \
                         --enable-static=no")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    
    
def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("authors", "ChangeLog", "readme", "copying")
