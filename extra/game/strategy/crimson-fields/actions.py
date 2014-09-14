#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "crimson-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-sound \
                         --enable-network \
                         --enable-cfed \
                         --enable-comet \
                         --enable-bi2cf \
                         --enable-cf2bmp")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README*", "THANKS", "TODO")
