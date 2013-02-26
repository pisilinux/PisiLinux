#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-rpath \
                         --disable-pinentry-gtk \
                         --enable-pinentry-curses \
                         --infodir=/usr/share/info")

def build():
    autotools.make()

def install():
    autotools.install()

    # We're using pinentry-wrapper as additional file instead of upstream pinentry symlink.
    pisitools.remove("/usr/bin/pinentry")

    pisitools.dosym("pinentry-gtk-2", "/usr/bin/pinentry-gtk")
    pisitools.dosym("pinentry-qt4", "/usr/bin/pinentry-qt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
