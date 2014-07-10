#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share/icons"]
# TODO: missing deps? liblocation, QtLocation, QtMobility

def setup():
    kde4.configure("-DQTONLY=ON \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=release")

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.remove("/usr/bin/marble-mobile")
    pisitools.remove("/usr/bin/marble-touch")
    pisitools.remove("/usr/share/applications/marble-mobile.desktop")
    pisitools.remove("/usr/share/applications/marble-touch.desktop")
    pisitools.dodoc("BUGS", "ChangeLog", "CODING", "COPYING*", "CREDITS", "LICENSE*", "MANIFESTO.txt", "TODO", "USECASES")
  