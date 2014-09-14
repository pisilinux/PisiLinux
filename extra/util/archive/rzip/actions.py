#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -O3 %s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("rzip")

    pisitools.doman("rzip.1")
    pisitools.dodoc("COPYING")
