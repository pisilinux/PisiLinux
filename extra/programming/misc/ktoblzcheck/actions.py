#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/python/Makefile.in", "py_compile = .*$", "py_compile = /bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-dependency-tracking \
                         --enable-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README")
