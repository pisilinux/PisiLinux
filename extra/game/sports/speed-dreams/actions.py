#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
			  -DCMAKE_INSTALL_PREFIX=/usr \
			  -DSD_BINDIR=/usr/bin \
			  -DSD_DATADIR=/usr/share/speed-dreams-2 \
			  -DSD_LIBDIR=/usr/lib/speed-dreams-2 \
			  -DOPTION_OFFICIAL_ONLY=ON")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES*", "README*", "COPYING*", "TODO*")