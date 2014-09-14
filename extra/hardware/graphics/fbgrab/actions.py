#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "gcc ", "\$(CC) ")
    pisitools.dosed("Makefile", "splint", "#splint")
    pisitools.dosed("Makefile", "-Wall", "-Wall %s %s" % (get.CFLAGS(), get.LDFLAGS()))

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    pisitools.dobin("fbgrab")

    pisitools.newman("fbgrab.1.man", "fbgrab.1")
