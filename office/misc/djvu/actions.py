#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "djvulibre-%s" % get.srcVERSION() if len(get.srcVERSION().split(".")) < 4 else "djvulibre-%s" % get.srcVERSION()[:get.srcVERSION().rfind(".")]

def setup():
    autotools.aclocal("-I config")
    autotools.autoconf("-f")

    autotools.configure("--enable-threads \
                         --disable-desktopfiles \
                         --enable-xmltools \
                         --enable-i18n \
                         --with-jpeg \
                         --with-tiff")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/mime/packages", "desktopfiles/djvulibre-mime.xml")

    for size in ["22", "32", "48", "64"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "desktopfiles/hi%s-djvu.png" % size, "image-vnd.djvu.png")

    pisitools.dodoc("COPY*", "README", "NEWS")
