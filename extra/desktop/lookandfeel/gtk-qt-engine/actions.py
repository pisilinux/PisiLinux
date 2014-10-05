#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir="gtk-qt-engine"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/icons/kcmgtk.png", "/usr/share/pixmaps")
    pisitools.removeDir("/usr/share/icons")

    #remove gtk-qt-engine's Qt4 engine, it causes some problems with Firefox 3
    pisitools.remove("/usr/lib/gtk-2.0/2.10.0/engines/libqt4engine.so")
    pisitools.removeDir("/usr/share/themes/Qt4")
    os.removedirs("%s/usr/share/themes" % get.installDIR())
