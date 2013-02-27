#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    for i in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(i)

    # autotools.autoreconf("-vfi -Im4")
    autotools.autoreconf("-vfi")

    # libtools.libtoolize("--force --install")
    autotools.configure("--disable-debugging \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("CHANGES", "COPYRIGHT", "CREDITS", "README", "TODO", "VERSION")
