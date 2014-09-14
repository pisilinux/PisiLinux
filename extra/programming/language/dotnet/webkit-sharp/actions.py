#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("MONO_SHARED_DIR", get.workDIR())

def setup():
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    # Empty files: NEWS, README
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
