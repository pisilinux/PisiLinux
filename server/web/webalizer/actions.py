#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="webalizer-2.23-05"

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.configure("--enable-bz2 \
                         --enable-geoip \
                         --with-dblib=/usr/lib/libdb.so")
def build():
    autotools.make()

def install():
    pisitools.dobin("webalizer")
    pisitools.dosym("/usr/bin/webalizer","/usr/bin/webazolver")
    pisitools.dodir("/usr/share/GeoDB")
    pisitools.doman("webalizer.1")
    pisitools.dodoc("*README*","CHANGES","Copyright")
