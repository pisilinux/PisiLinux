#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CC=.*", "CC = %s" % get.CC())
    pisitools.dosed("Makefile", "CFLAGS=.*", "CFLAGS = %s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("e00conv")
    pisitools.doman("e00conv.1")
    pisitools.dodoc("e00compr.html", "e00compr.txt", "ex_write*.c", "ex_read*.c")
