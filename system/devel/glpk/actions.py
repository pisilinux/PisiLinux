#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    if get.buildTYPE() != "emul32":
        pisitools.flags.add("-fPIC")

    autotools.configure("--disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("CFLAGS=-O2 LDFLAGS=-s")

def install():
    autotools.install()

    pisitools.dodoc("README", "ChangeLog", "NEWS", "COPYING", "AUTHORS")

