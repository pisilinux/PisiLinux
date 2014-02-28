#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("--enable-static=no \
                         --enable-introspection=yes")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.domove("/usr/share/gtk-doc/html/gtkextra/*", "/usr/share/gtk-doc/html/gtkextra3")
    pisitools.removeDir("/usr/share/gtk-doc/html/gtkextra/")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")