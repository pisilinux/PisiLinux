#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#cpuparameter = "" if get.ARCH() == "x86_64" else "--enable-mmx"

#def setup():
#    autotools.configure("--disable-static \
#                           %s" % cpuparameter)

def setup():
    autotools.configure("--prefix=/usr \
                         --libdir=/usr/lib \
                         --disable-static \
                         --enable-mmx")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
