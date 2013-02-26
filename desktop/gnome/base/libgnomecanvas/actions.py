#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static\
                         --enable-glade")

#    pisitools.dosed("libgnomecanvas/Makefile", "^LIBS = (.*)$", "LIBS = \\1 -lm")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS")
