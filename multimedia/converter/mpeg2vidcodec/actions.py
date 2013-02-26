#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
