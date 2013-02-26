#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-glibtest \
                         --disable-gtktest \
                         --with-gdktarget=x11 \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "AUTHORS", "ChangeLog*", "COPYING*", "TODO")
