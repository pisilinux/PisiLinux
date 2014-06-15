#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

if get.ARCH()== "x86_64": e64 = " --enable-64bit"
else: e64 = ''

def setup():
    #pisitools.dosed("configure", "--libmysqld-libs", "--libs")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --datadir=/usr/share/grass \
                         --with-proj \
                         --with-proj-includes=/usr/include \
                         --with-proj-libs=/usr/lib \
                         --with-proj-share=/usr/share/proj \
                         --with-gdal \
                         --with-png \
                         --with-tiff \
                         --with-tcltk \
                         --without-glw \
                         --with-postgres \
                         --with-opengl \
                         --with-fftw \
                         --with-nls \
                         --with-geos \
                         --with-python \
                         --with-freetype=yes \
                         --with-wxwidgets=/usr/bin/wx-config-2.8 \
                         --with-postgres-includes=/usr/include/postgresql \
                         --with-freetype-includes=/usr/include/freetype2 \
                         --with-nls%s" % e64)

def build():
    autotools.make("htmldocs-single")
    autotools.make()

def install():
    autotools.install()
    gw = get.srcVERSION().replace('.',  '')[:-1]
    print gw
    for i in ["AUTHORS", "CHANGES", "COPYING", "GPL.TXT", "REQUIREMENTS.html"]:
        pisitools.domove("/usr/lib/grass%s/%s" % (gw, i),  "/usr/share/doc/grass/")
    pisitools.domove("/usr/lib/grass%s/docs/html" % gw,  "/usr/share/doc/grass/html")
    pisitools.remove("/usr/lib/grass%s/docs" % gw)
    pisitools.domove("/usr/lib/grass%s/include/grass" % gw, "/usr/include")
    pisitools.insinto("/usr/lib/pkgconfig", "grass.pc")
    pisitools.dosed("%s/usr/bin/grass%s" % (get.installDIR(), gw), "(GISBASE=).*install(.*)", r"\1\2")
