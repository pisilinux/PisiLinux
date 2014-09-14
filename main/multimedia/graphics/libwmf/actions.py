#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

def setup():
    shelltools.unlink("configure.ac")
    shelltools.sym("patches/acconfig.h", "acconfig.h")

    autotools.autoreconf("-fi")
    pisitools.dosed("src/Makefile.in", "@LIBWMF_GDK_PIXBUF_TRUE@", "#")
    autotools.configure("--without-expat \
                         --with-libxml2 \
                         --with-jpeg \
                         --with-x \
                         --with-gsfontdir=/usr/share/fonts/default/ghostscript \
                         --with-fontdir=/usr/share/libwmf/fonts \
                         --with-docdir=/usr/share/doc/%s \
                         --disable-static" % get.srcNAME() )
def build():
    autotools.make("LIBTOOL=/usr/bin/libtool")

def install():
    pisitools.dosed("fonts/fontmap", "libwmf/fonts", "fonts/default/ghostscript")

    autotools.rawInstall("DESTDIR=%s \
                          fontdir=/usr/share/libwmf/fonts \
                          wmfonedocdir=/usr/share/doc/%s/caolan \
                          wmfdocdir=/usr/share/doc/%s" %
                          ( get.installDIR(), get.srcNAME(), get.srcNAME() ) )

    if shelltools.isDirectory("%s/usr/lib/gtk-2.0" % get.installDIR()):
        # seems "/usr/lib/gtk-2.0" no longer exists, so need check
        pisitools.removeDir("/usr/lib/gtk-2.0")

    # These fonts included in gnu-gs-fonts-std package.
    pisitools.remove("/usr/share/libwmf/fonts/*afm")
    pisitools.remove("/usr/share/libwmf/fonts/*pfb")

    pisitools.dodoc("README", "AUTHORS", "CREDITS", "ChangeLog", "NEWS", "TODO")
