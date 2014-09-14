#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial=["libtool"]

def setup():
    pisitools.dosed("configure.ac", "AC_PATH_XTRA")
    autotools.autoreconf("-fi")

    pisitools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure("--with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --docdir=/usr/share/doc/imagemagick \
                         --enable-hdri \
                         --enable-shared \
                         --disable-static \
                         --with-modules \
                         --with-perl \
                         --with-perl-options='INSTALLDIRS=vendor' \
                         --with-x \
                         --with-threads \
                         --with-magick_plus_plus \
                         --with-gslib \
                         --with-wmf \
                         --with-lcms2 \
                         --with-rsvg \
                         --with-xml \
                         --with-djvu \
                         --with-bzlib \
                         --with-zlib \
                         --with-fpx \
                         --with-tiff \
                         --with-jp2 \
                         --with-jpeg \
                         --without-jbig \
                         --without-fpx \
                         --without-dps")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE", "NEWS.txt")

    pisitools.remove("/usr/lib/*.la")

    perlmodules.removePacklist()
    perlmodules.removePodfiles()
