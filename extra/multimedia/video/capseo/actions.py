#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lib%s" % get.srcDIR().split("_")[0]

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-debug \
                         --enable-examples \
                         --enable-theora \
                         --enable-tools")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
