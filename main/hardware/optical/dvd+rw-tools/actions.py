#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.m4", "^CFLAGS.*\+=\$\(WARN\).*", "CFLAGS=" + get.CFLAGS())
    pisitools.dosed("Makefile.m4", "^CXXFLAGS+=\$\(WARN\).*", "CXXFLAGS=" + get.CXXFLAGS() + " -fno-exceptions")

def build():
    autotools.make("CC='%s' CXX='%s'" % (get.CC(), get.CXX()))

def install():
    pisitools.dobin("dvd+rw-booktype")
    pisitools.dobin("dvd+rw-format")
    pisitools.dobin("dvd+rw-mediainfo")
    pisitools.dobin("dvd-ram-control")
    pisitools.dobin("growisofs")

    pisitools.dohtml(".")
    pisitools.doman("growisofs.1")
