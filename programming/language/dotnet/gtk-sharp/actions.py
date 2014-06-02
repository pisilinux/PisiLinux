#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    #autotools.autoreconf("-fi")
    shelltools.system("./bootstrap-2.12")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.install()
