#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="ftgl-%s" % get.srcVERSION().replace("_", "~")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static")
def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "TODO")

