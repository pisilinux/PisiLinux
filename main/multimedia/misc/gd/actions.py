#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--disable-static \
                         --with-fontconfig \
                         --with-png \
                         --with-freetype \
                         --with-jpeg \
                         --without-xpm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml(".")
    pisitools.dodoc("COPYING", "NEWS", "ChangeLog")
