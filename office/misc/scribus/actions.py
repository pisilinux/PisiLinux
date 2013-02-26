#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde4


WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "."))

def setup():
    # Remove version info from doc dir
    pisitools.dosed("CMakeLists.txt", "\"share\/doc\/\$\{MAIN_DIR_NAME\}.*", "\"share/doc/${MAIN_DIR_NAME}/\")")
    kde4.configure("-DWANT_DISTROBUILD=YES")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.insinto("/usr/share/pixmaps", "resources/icons/scribus.png")
    pisitools.insinto("/usr/share/pixmaps", "resources/icons/scribusdoc.png", "x-scribus.png")
