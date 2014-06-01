#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DQT_MKSPECS_RELATIVE=share/qt4/mkspecs \
                          -DEIGEN2_INCLUDE_DIR=/usr/include/eigen2 \
                          -DPYTHON_LIBRARY:PATH='/usr/lib/lib%s.so'" % get.curPYTHON() )

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/pixmaps/avogadro-icon.png", "/usr/share/pixmaps/avogadro.png")

    pisitools.dodoc("ChangeLog", "COPYING", "AUTHORS")
