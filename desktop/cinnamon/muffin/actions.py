#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --libexecdir=/usr/lib/muffin \
			 --localstatedir=/var \
			 --disable-static \
			 --enable-compile-warnings=no \
			 --disable-static \
			 --enable-shape \
			 --enable-sm \
			 --enable-startup-notification \
			 --enable-xsync \
			 --enable-verbose-mode \
			 --enable-compile-warnings=maximum \
			 --with-libcanberra")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
