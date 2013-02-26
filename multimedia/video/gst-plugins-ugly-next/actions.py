#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    # sidplay is in contrib.
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-sidplay \
                         --with-package-name=\"Pardus gstreamer-plugins-ugly package\" \
                         --with-package-origin=\"http://www.pardus-anka.org/eng\"")

def build():
    autotools.make()

# causes sandbox violations
#def check():
#    # causes sandbox violation
#    shelltools.export("HOME", get.workDIR())
#    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.dodoc("README", "COPYING", "AUTHORS", "NEWS")
