#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DWANT_SVN_STAMP=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

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
    pisitools.insinto("/usr/share/megaglest", "glestuser.ini")
    pisitools.insinto("/usr/share/megaglest", "glestuserkeys.ini")
    pisitools.insinto("/usr/share/megaglest", "servers.ini")

    # Documentations
    pisitools.dodoc("AUTHORS*", "CHANGELOG*", "COPYRIGHT*", "gnu_gpl_3.0.txt", "README*")
