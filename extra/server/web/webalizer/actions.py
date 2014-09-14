#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="webalizer-2.23-08"

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
    pisitools.dodir("/usr/share/webalizer/flags")

    pisitools.insinto("/usr/share/GeoDB","../GeoDB.dat")
    pisitools.insinto("/usr/share/GeoDB","../GEODB.README")
    pisitools.insinto("/usr/share/webalizer/flags","../flags/*")

    pisitools.doman("webalizer.1")
    pisitools.dodoc("*README*","CHANGES","Copyright")
