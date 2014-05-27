#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("\
                         --disable-static \
                         --with-pic \
                         --enable-introspection=yes \
                         --enable-cairo=yes \
                         --enable-gdk-pixbuf=yes \
                         --enable-cogl-pango=yes \
                         --enable-glx=yes \
                         --enable-gles1=yes \
                         --enable-gles2=yes \
                        ")
                        
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")

