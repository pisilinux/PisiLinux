#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
			 --enable-tracker-backend \
			 --enable-libsocialweb-backend=auto \
			 --disable-schemas-compile \
			 --enable-eds-backend \
			 --enable-vala \
			 --enable-inspect-tool \
			 --enable-import-tool")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "AUTHORS", "COPYING")
