#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "devil-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")

    autotools.configure("--disable-dependency-tracking \
                         --enable-bmp=no \
                         --enable-jpeg=yes \
                         --enable-ILU \
                         --enable-ILUT \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "NEWS", "README*", "*.txt")
