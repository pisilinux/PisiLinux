#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fsigned-char -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --with-gsm \
                         --with-dyn-default")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README", "NEWS", "AUTHORS", "COPYING", "LICENSE*")
