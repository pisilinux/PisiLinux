#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mpeg2"

def setup():
     pisitools.dosed("Makefile", "-O2", get.CFLAGS())

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    pisitools.dobin("src/mpeg2dec/mpeg2decode")
    pisitools.dobin("src/mpeg2enc/mpeg2encode")

    pisitools.dodoc("README", "doc/*")
