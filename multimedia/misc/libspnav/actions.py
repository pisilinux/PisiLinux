#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-opt --enable-ldopt")
def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/", "*.so*")
    pisitools.domove("/usr/lib/libspnav.so.0.1", "/usr/lib", "libspnav.so")
    pisitools.insinto("/usr/lib/", "*.so*")
    pisitools.insinto("/usr/include/", "*.h")

    pisitools.dodoc("README")
