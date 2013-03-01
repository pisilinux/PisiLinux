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
                         --enable-gtk3 \
                         --enable-alsa \
                         --enable-null \
                         --enable-gtk \
                         --enable-tdb \
                         --with-builtin=dso \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.removeDir("/usr/share/gnome")
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("LGPL", "README")
