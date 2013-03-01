#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DENABLE_FGADMIN=OFF \
                          -DENABLE_PROFILE=OFF \
                          -DENABLE_RTI=OFF \
                          -DFG_DATA_DIR=/usr/share/flightgear \
                          -DSIMGEAR_SHARED=ON \
                          -DSP_FDMS=OFF \
                          -DSYSTEM_SQLITE=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README*", "ChangeLog", "AUTHORS", "NEWS", "Thanks")
