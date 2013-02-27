#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = "%s-2.3_1-opensource" % get.srcNAME()
INCLUDE_DIR = "/usr/include/QtSolutions"

def setup():
    shelltools.touch(".licenseAccepted")
    autotools.rawConfigure("-library")

def build():
    qt4.configure()
    autotools.make()

def install():
    pisitools.insinto(INCLUDE_DIR, "src/QtIOCompressor")
    pisitools.insinto(INCLUDE_DIR, "src/qtiocompressor.h")

    pisitools.insinto("/usr/lib", "lib/*")

    pisitools.dodoc("LICENSE*", "README.TXT")
