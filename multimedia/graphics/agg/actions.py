#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("authors", "ChangeLog", "readme", "copying")
