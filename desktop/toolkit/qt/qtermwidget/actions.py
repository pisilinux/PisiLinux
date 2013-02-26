# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("src/test")
    pisitools.rename("/usr/bin/test", "consoleq")

    pisitools.remove("/usr/include/qtermwidget.h")
    pisitools.insinto("/usr/include/qtermwidget", "lib/*.h")

    pisitools.dodoc("AUTHORS", "README", "COPYING")

"""
def install():
    # Binaries
    pisitools.dobin("consoleq", "/usr/bin")
    pisitools.dobin("consoleq_d", "/usr/bin")

    # Libs
    pisitools.dolib("libqtermwidget*")

    # Headers
    pisitools.insinto("/usr/include/qtermwidget", "lib/*.h")

    # Docs
    pisitools.dodoc("AUTHORS", "README", "COPYING")
"""
