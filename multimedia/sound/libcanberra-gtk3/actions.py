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
                         --enable-gtk3 \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    
    pisitools.removeDir("/usr/include")
    pisitools.remove("/usr/lib/libcanberra-gtk.so.0.1.9")
    pisitools.remove("/usr/lib/libcanberra.so.0")
    pisitools.remove("/usr/lib/libcanberra-gtk.so.0")
    pisitools.remove("/usr/lib/libcanberra.so")
    pisitools.remove("/usr/lib/libcanberra.so.0.2.5")
    pisitools.remove("/usr/lib/libcanberra-gtk.so")
    pisitools.remove("/usr/lib/pkgconfig/libcanberra-gtk.pc")
    pisitools.remove("/usr/lib/pkgconfig/libcanberra.pc")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.removeDir("/usr/share/vala")
    pisitools.removeDir("/usr/share/doc/libcanberra")
    pisitools.removeDir("/usr/lib/libcanberra-0.30")
    pisitools.removeDir("/usr/lib/gtk-2.0")
    pisitools.removeDir("/usr/lib/gnome-settings-daemon-3.0")
    pisitools.removeDir("/usr/share/gdm")
    pisitools.removeDir("/usr/share/gnome")

    pisitools.dodoc("LGPL", "README")