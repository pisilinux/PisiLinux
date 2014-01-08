#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("themes/Adwaita/gtk-3.0/gtk-widgets.css", "@menu_bg_color;", "transparent;")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README")
