#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("script/*", "/usr/bin/env python", "/usr/bin/python")
    pythonmodules.compile()

def install():
    pythonmodules.install("--no-version-script \
                           --standalone-lib \
                           --install-scripts=/usr/bin \
                           --install-data=/usr/share")

    pisitools.dodoc("CHANGES*", "LICENSE*", "README*", "RELEASE*")
