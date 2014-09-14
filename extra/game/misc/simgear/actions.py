#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DJPEG_FACTORY=ON \
                          -DENABLE_TESTS=OFF \
                          -DSIMGEAR_SHARED=ON \
                          -DSYSTEM_EXPAT=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*", "NEWS", "AUTHORS", "ChangeLog")