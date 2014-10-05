#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules


def build():
    shelltools.cd("linux")
    pythonmodules.compile()

def install():
    pisitools.dodoc("CREDITS", "LAYOUT", "README")

    shelltools.cd("linux")
    pythonmodules.install()
