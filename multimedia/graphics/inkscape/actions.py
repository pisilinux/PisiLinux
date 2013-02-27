#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #we've patches changing configure.ac
    autotools.autoreconf('-vfi')

    autotools.configure("--with-gnome-vfs \
                         --enable-lcms \
                         --enable-poppler-cairo \
                         --disable-dependency-tracking \
                         --with-python \
                         --with-perl")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
