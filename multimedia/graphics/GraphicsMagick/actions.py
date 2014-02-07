#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

# .la files needed to load modules
KeepSpecial = ["libtool"]

def setup():
    # ghostscript is better than dps
    # unstable fpx support disabled
    # trio is for old systems not providing vsnprintf
    autotools.configure("--enable-openmp \
                         --enable-shared \
                         --disable-static \
                         --with-threads \
                         --with-modules \
                         --with-magick-plus-plus \
                         --with-perl \
                         --with-bzlib \
                         --without-dps \
                         --without-fpx \
                         --with-gslib \
                         --with-jbig \
                         --with-jpeg \
                         --with-jp2 \
                         --with-lcms \
                         --with-png \
                         --with-tiff \
                         --without-trio \
                         --with-ttf \
                         --with-wmf \
                         --with-fontpath=/usr/share/fonts \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --with-xml \
                         --with-zlib \
                         --with-x \
                         --with-quantum-depth=16")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("perl-build")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C PerlMagick" % get.installDIR())
    for d in ("demo/", "Changelog", "README.txt"):
        pisitools.insinto("/usr/share/doc/PerlMagick", "PerlMagick/%s" % d)

    pisitools.remove("/usr/lib/*.la")
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
