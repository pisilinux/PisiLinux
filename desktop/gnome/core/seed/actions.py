#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
			 --with-webkit=3.0 \
			 --enable-readline-module \
			 --enable-os-module \
			 --enable-ffi-module \
			 --enable-gtkbuilder-module \
			 --enable-cairo-module \
			 --enable-gettext-module \
			 --enable-dbus-module \
			 --enable-mpfr-module \
			 --enable-sqlite-module \
			 --enable-libxml-module")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "NEWS", "README")

