#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    pisitools.cflags.add("-fno-strict-aliasing")

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
                         --with-netcdf=/usr/lib/netcdf \
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
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
