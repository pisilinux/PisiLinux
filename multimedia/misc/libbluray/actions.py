#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("JAVA_HOME", "/opt/sun-jdk")

def setup():
    autotools.autoreconf("-vif")
    # Some of the examples need the static lib to build.
    # Don't build them if not building the static lib too.
    autotools.configure("--disable-static \
                         --disable-bdjava")

def build():
    autotools.make()
    #autotools.make("doxygen-pdf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "README.*")
