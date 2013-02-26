#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
