# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-v%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    cmaketools.configure("-DAUTOPLUGINS=1")

    shelltools.system("lrelease QDevelop.pro")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.insinto("/usr/share/applications", "qdevelop.desktop")
    pisitools.insinto("/usr/share/pixmaps", "resources/images/logo.png", "qdevelop.png")

    pisitools.dodoc("ChangeLog.txt", "README.txt", "copying")
