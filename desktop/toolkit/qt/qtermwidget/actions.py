# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON -DCMAKE_INSTALL_LIBDIR=lib")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#    pisitools.dobin("src/test")
#    pisitools.rename("/usr/bin/test", "consoleq")

    pisitools.remove("/usr/include/qtermwidget4/qtermwidget.h")
    pisitools.insinto("/usr/include/qtermwidget4", "lib/*.h")
    pisitools.insinto("/usr/lib/pkgconfig", "qtermwidget4.pc")

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
