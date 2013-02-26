#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("configure.in", "-ffast-math")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "NEWS", "TODO", "AUTHORS", "ChangeLog")
