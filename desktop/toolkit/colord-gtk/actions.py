#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-gtk-doc \
                         --enable-vala \
                         --disable-static \
                         --disable-rpath \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")