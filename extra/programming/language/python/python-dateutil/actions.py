#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.remove("/usr/lib/%s/site-packages/dateutil/zoneinfo/*.tar.gz" % get.curPYTHON())
    pisitools.dodoc("example.py", "LICENSE", "NEWS", "README")
