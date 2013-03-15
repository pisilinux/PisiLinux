#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()

    shelltools.cd("plugins")
    qt4.configure()
    qt4.make()

def install():
    pisitools.dobin("unix/librecad")

    pisitools.insinto("/usr/share/applications/", "desktop/librecad.desktop")
    pisitools.insinto("/usr/share/mime/packages/", "desktop/librecad.sharedmimeinfo", "librecad.xml")
    pisitools.insinto("/usr/share/pixmaps/", "res/main/librecad.png")

    pisitools.insinto("/usr/share/librecad/fonts/", "unix/resources/fonts/*")
    pisitools.insinto("/usr/share/librecad/library/", "unix/resources/library/*")
    pisitools.insinto("/usr/share/librecad/patterns/", "unix/resources/patterns/*")
    pisitools.insinto("/usr/share/librecad/qm/", "unix/resources/qm/*")
    pisitools.insinto("/usr/share/librecad/plugins/", "unix/resources/plugins/*")

    pisitools.dodoc("README", "gpl-2.0.txt")
