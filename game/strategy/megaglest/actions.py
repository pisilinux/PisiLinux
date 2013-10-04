#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

#import os
#shelltools.export("LC_ALL -c", get.workDIR())



def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DWANT_SVN_STAMP=OFF \
                          -no-discard-stderr \
                          -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr" ,sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")

    # Lets install a nice icon for desktop files
    pisitools.insinto("/usr/share/pixmaps", "megaglest.png")

    # Remove Windows icon files, we don't need them
    pisitools.remove("/usr/share/pixmaps/*.ico")
    pisitools.remove("/usr/share/pixmaps/*.bmp")

    # And now we install desktop file
    pisitools.insinto("/usr/share/applications", "megaglest.desktop")

    # Configurations
    pisitools.insinto("/usr/share/megaglest", "glest.ini")
    pisitools.insinto("/usr/share/megaglest", "glestkeys.ini")
    pisitools.insinto("/usr/share/megaglest", "servers.ini")

    # Documentations
    pisitools.dodoc("AUTHORS*", "CHANGELOG*", "COPYRIGHT*", "gnu_gpl_3.0.txt", "README*")