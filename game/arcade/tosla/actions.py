#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install()

    pisitools.dosym("/usr/share/tosla/start.py", "/usr/bin/tosla")
    pisitools.dodoc("README.txt","AUTHORS.txt","COPYING.txt")
