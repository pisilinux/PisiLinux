#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libtorrent-rasterbar-%s" % get.srcVERSION()


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-python-binding \
                         --enable-encryption \
                         --with-boost-filesystem=mt \
                         --with-boost-thread=mt \
                         --with-zlib=system \
                         --with-libgeoip=system")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/bin")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
