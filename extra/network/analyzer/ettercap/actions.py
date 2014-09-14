#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DENABLE_GTK=ON -DCMAKE_INSTALL_PREFIX=/usr -DINSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    shelltools.cd("..")
    pisitools.insinto("/usr/share/pixmaps", "share/ettercap.png")
    pisitools.insinto("/usr/share/applications", "desktop/ettercap.desktop")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README*", "TODO*")