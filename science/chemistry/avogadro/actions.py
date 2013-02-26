#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_THREADGL=FALSE \
                            -DENABLE_RPATH=OFF \
                            -DENABLE_UPDATE_CHECKER=OFF \
                            -DPYTHON_LIBRARY:PATH='/usr/lib/lib%s.so'" % get.curPYTHON() )

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/pixmaps/avogadro-icon.png", "/usr/share/pixmaps/avogadro.png")

    pisitools.dodoc("ChangeLog", "COPYING", "AUTHORS")
