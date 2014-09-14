#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

def setup():
    pisitools.dosed("ogr/ogrsf_frmts/sqlite/ogr_sqlite.h", "spatialite/sqlite3.h", "sqlite3.h")
    libtools.libtoolize()
    autotools.autoreconf("-vfi")
    autotools.aclocal()
    pisitools.cflags.add("-fno-strict-aliasing")
    pisitools.dosed("configure", "-L\$with_cfitsio -L\$with_cfitsio/lib -lcfitsio", "-lcfitsio")
    pisitools.dosed("configure", "-I\$with_cfitsio -I\$with_cfitsio/include", "-I\$with_cfitsio/include/cfitsio")
    pisitools.dosed("configure", "-lnetcdf -L\$with_netcdf -L\$with_netcdf/lib \$LIBS", "-lnetcdf $LIBS")
    pisitools.dosed("configure", "-L\$DODS_LIB -ldap\+\+", "-ldap++")
    pisitools.dosed("configure", "-L\$with_ogdi -L\$with_ogdi/lib -logdi", "-logdi")
    pisitools.dosed("configure", "-L\$with_jpeg -L\$with_jpeg/lib -ljpeg", "-ljpeg")
    pisitools.dosed("configure", "-L\$with_libtiff\/lib -ltiff", "-ltiff")
    pisitools.dosed("configure", "-lgeotiff -L\$with_geotiff \$LIBS", "-lgeotiff $LIBS")
    pisitools.dosed("configure", "-L\$with_geotiff\/lib -lgeotiff \$LIBS", "-lgeotiff $LIBS")
    pisitools.dosed("ogr/ogrct.cpp", "libproj.so", "libproj.so.0")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --datadir=/usr/share/gdal \
                         --with-ogdi \
                         --with-threads \
                         --with-jasper \
                         --with-odbc=/usr/lib/unixODBC \
                         --with-expat \
                         --with-cfitsio \
                         --with-hdf5 \
                         --with-netcdf \
                         --with-png \
                         --with-geos \
                         --without-mysql \
                         --with-curl \
                         --with-perl \
                         --with-jpeg \
                         --with-jpeg12=no \
                         --with-libtiff \
                         --with-sqlite3 \
                         --with-geotiff=external \
                         --with-podofo \
                         --with-spatialite \
                         --with-ogr \
                         --with-grib \
                         --with-curl \
                         --with-webp \
                         --with-python \
                         --without-poppler \
                         --with-xerces \
                         --without-openjpeg \
                         --without-libtool \
                         --without-hdf4 \
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
                         --without-ruby")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    shelltools.cd("swig/perl")
    perlmodules.configure()
    pisitools.dosed("Makefile_*"," -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.cd("swig/perl")
    perlmodules.make()
    shelltools.cd("../..")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #remove egg
    pisitools.removeDir("/usr/lib/python2.7/site-packages/GDAL-*")

    perlmodules.removePodfiles()
