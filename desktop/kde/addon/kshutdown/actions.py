#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

WorkDir = "kshutdown-%s" % get.srcVERSION().replace('_','').rstrip("1")
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/kshutdown.png", "/usr/share/pixmaps/kshutdown.png")

    pisitools.dodoc("LICENSE",  "ChangeLog", "TODO")
    pisitools.dohtml("README.html")
