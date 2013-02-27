#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-cups \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "THANKS")

    pisitools.dosym("/usr/share/epdfview/pixmaps/icon_epdfview-48.png", "/usr/share/pixmaps/epdfview.png")

