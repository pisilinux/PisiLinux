#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()

    # perl has some libtool problems right now, disabled
    autotools.configure("--disable-static \
                         --datadir=/usr/share/gdal \
                         --with-ogdi \
                         --with-threads \
                         --with-jasper \
                         --with-odbc=/usr/lib/unixODBC \
                         --with-expat \
                         --with-cfitsio \
                         --with-hdf5 \
                         --without-mrsid \
                         --without-netcdf \
                         --without-hdf4 \
                         --without-grass \
                         --without-fme \
                         --without-pcraster \
                         --without-kakadu \
                         --without-mrsid \
                         --without-jp2mrsid \
                         --without-msg \
                         --without-bsb \
                         --without-dods-root \
                         --without-oci \
                         --without-ingres \
                         --without-spatialite \
                         --without-dwgdirect \
                         --without-epsilon \
                         --without-idb \
                         --without-sde \
                         --with-geos \
                         --with-mysql \
                         --with-curl \
                         --with-perl \
                         --with-jpeg \
                         --with-jpeg12=no \
                         --without-ruby \
                         --without-perl \
                         --without-php")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
