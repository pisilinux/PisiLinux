#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
