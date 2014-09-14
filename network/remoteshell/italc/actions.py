#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_DIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/italc")

    pisitools.insinto("/usr/share/pixmaps", "ima/data/italc.png", "ica.png")
    pisitools.insinto("/usr/share/pixmaps", "ima/resources/fullscreen_demo.png", "italc.png")

    pisitools.dodoc("AUTHORS", "README", "TODO", "ChangeLog", "COPYING")
