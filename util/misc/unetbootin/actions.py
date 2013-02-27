#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("lupdate unetbootin.pro")
    shelltools.system("lrelease unetbootin.pro")
    qt4.configure()

def build():
    qt4.make()
    pisitools.dosed("unetbootin.desktop","Exec=/usr/bin/unetbootin",
        "Exec=xdg-su -c /usr/bin/unetbootin")
    pisitools.dosed("unetbootin.desktop","Icon=unetbootin",
        "Icon=/usr/share/pixmaps/unetbootin.png")

def install():
    pisitools.dobin("unetbootin")
    pisitools.insinto("/usr/share/applications","unetbootin.desktop")
    for size in ["14","16","22","24","32","48","64","128","192","256","512"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/" % (size, size),
            "unetbootin_%s.png" % size)
    pisitools.dosym("/usr/share/icons/hicolor/64x64/unetbootin_64.png",
        "/usr/share/pixmaps/unetbootin.png")
    pisitools.insinto("/usr/share/unetbootin","unetbootin*.qm")
    pisitools.dodoc("INSTALL", "README*")
    
