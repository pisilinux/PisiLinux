#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --libexecdir=/usr/lib/mate-document-viewer \
				    --disable-static \
				    --disable-rpath \
				    --enable-caja \
				    --enable-pdf \
				    --enable-tiff \
				    --enable-djvu \
				    --enable-dvi \
				    --enable-xps \
				    --enable-t1lib \
				    --enable-comics \
				    --enable-pixbuf \
				    --enable-impress \
				    --disable-scrollkeeper \
				    --disable-introspection \
				    --disable-schemas-compile \
				    --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
