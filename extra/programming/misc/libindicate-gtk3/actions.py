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
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gtk=3 \
                         --disable-scrollkeeper \
                         --disable-gtk-doc \
                         --enable-introspection=yes \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/usr/lib/python2.7")
    pisitools.remove("/usr/lib/libindicate.so*")
    pisitools.remove("/usr/lib/pkgconfig/indicate-0.7.pc")
    pisitools.remove("/usr/lib/girepository-1.0/Indicate-0.7.typelib")
    pisitools.removeDir("/usr/share/doc/libindicate")
    pisitools.removeDir("/usr/share/gtk-doc/")
    pisitools.removeDir("/usr/share/vala/")
    pisitools.removeDir("/usr/share/gir-1.0")
    pisitools.removeDir("/usr/share/pygtk/")
    
    pisitools.removeDir("/usr/include/libindicate-0.7")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README", "NEWS")