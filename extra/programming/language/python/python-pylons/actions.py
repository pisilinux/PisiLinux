#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

#WorkDir = "Pylons-pylons-c4d26be"

def install():
    pythonmodules.install()

    pisitools.dodoc("UPGRADING")
