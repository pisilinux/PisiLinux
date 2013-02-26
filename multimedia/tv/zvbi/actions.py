#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-nls \
                         --with-x \
                         --enable-v4l \
                         --enable-dvb \
                         --with-doxygen")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("ChangeLog", "AUTHORS", "COPYING", "NEWS", "README*", "TODO")
