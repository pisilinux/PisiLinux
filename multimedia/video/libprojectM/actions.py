#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CXXFLAGS", "%s -lGL" % get.CXXFLAGS())

def setup():
    cmaketools.configure("-Wno-dev \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DINCLUDE-PROJECTM-JACK=ON ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING.txt")
