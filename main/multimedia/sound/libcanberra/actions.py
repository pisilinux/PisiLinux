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
    autotools.autoreconf("-fi")
    autotools.configure("--disable-oss \
                         --disable-lynx \
                         --disable-gtk-doc \
                         --disable-schemas-install \
                         --enable-gstreamer \
                         --enable-pulse \
                         --enable-alsa \
                         --enable-null \
                         --enable-tdb \
                         --with-builtin=dso \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    
    #pisitools.remove("/usr/lib/gtk-3.0/modules/libcanberra-gtk-module.so")
    pisitools.removeDir("/usr/share/gtk-doc")
    
    pisitools.dodoc("LGPL", "README")
