#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-experimental \
                         --with-package-name='PisiLinux gstreamer-plugins-base package' \
                         --with-package-origin='http://www.pisilinux.org'")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

# tests fail sandbox
#def check():
#    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
