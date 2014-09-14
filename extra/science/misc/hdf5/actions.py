#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-cxx \
                         --enable-hl \
                         --enable-threadsafe \
                         --enable-fortran \
                         --enable-production \
                         --enable-linux-lfs \
                         --enable-unsupported \
                         --disable-static \
                         --disable-parallel \
                         --disable-sharedlib-rpath \
                         --disable-dependency-tracking \
                         --docdir=/usr/share/doc/hdf5/ \
                         --with-pthread=/usr/lib/ \
                         --with-pic")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ACKNOWLEDGMENTS", "COPYING", "README*", "release_docs/HISTORY-*", "release_docs/RELEASE.txt")
