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
    shelltools.export("CXXFLAGS", "%s -DUSE_STATIC_CONF" % get.CFLAGS())

    autotools.autoconf()
    autotools.configure("--without-scglib")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "CREDITS", "ChangeLog", "NEWS", "README*")

