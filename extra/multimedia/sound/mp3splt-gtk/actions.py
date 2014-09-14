#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("mp3splt-gtk.desktop.in", "PREFIX/", "")
    autotools.configure("--disable-rpath \
                         --disable-doxygen_doc \
                         --disable-audacious \
                         --disable-gnome \
                         --disable-gtk3\
                         --enable-gtk2")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")