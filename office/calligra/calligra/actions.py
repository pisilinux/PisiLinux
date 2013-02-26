#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get
import os

shelltools.export("HOME", get.workDIR())

def setup():
        kde4.configure("-DIHAVEPATCHEDQT=1 \
			-DCMAKE_SKIP_RPATH=ON \
			-DCMAKE_BUILD_TYPE=Release \
			-DBUILD_active=OFF \
			-DBUILD_cstester:BOOL=OFF \
			-DKDE4_BUILD_TESTS=OFF \
			-DBUILD_mobile=OFF \
			-DCMAKE_INSTALL_PREFIX=/usr ")

def build():
    kde4.make()

def install():
    kde4.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README", "doc/status.txt")
