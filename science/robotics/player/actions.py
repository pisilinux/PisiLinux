#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_RUBYCPP_BINDINGS=ON \
			  -DBoost_USE_MULTITHREAD=ON \
			  -DUNICAP_DIR=/usr \
			  -DBUILD_PLAYERCC_BOOST=ON \
			  -DBUILD_PYTHONC_BINDINGS=ON \
			  -DBUILD_PYTHONCPP_BINDINGS=ON \
			  -DBUILD_EXAMPLES=ON \
			  -DBUILD_DOCUMENTATION=ON \
			  -DBUILD_PLAYERCC=ON \
			  -DSWIG_EXECUTABLE=/usr/bin/swig")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

    # Move examples under doc dir
    pisitools.domove("usr/share/player/examples", "usr/share/doc/" + get.srcNAME())
