#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "SFML_BUILD_DOC FALSE", "SFML_BUILD_DOC TRUE")

    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/SFML", "examples/*")

    pisitools.dodoc("license.txt", "readme.txt")
