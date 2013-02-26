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

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -fomit-frame-pointer -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" \
                    LDFLAGS="%s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("tree")

    pisitools.doman("doc/tree.1")
    pisitools.dodoc("CHANGES", "README*")
