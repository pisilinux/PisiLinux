#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shapefile=yes \
                         --enable-pdb=yes \
                         --enable-csv=yes \
                         --enable-filters=yes \
                         --with-cet=all \
                         --with-zlib=system \
                         --with-expathdr=/usr/include \
                         --with-libexpat=/usr/lib \
                         --with-doc=/usr/share/doc/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    pisitools.dobin("gpsbabel")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
#    pisitools.dohtml("gpsbabel.html")
    pisitools.dohtml("gui/help/gpsbabel.html")
