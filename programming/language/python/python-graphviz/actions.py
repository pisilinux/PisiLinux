#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("setup.py", "docdirbase  = .*", "docdirbase = 'share/doc/%s'" % get.srcNAME())

def install():
    pythonmodules.install()

    pisitools.remove("/usr/share/doc/%s/INSTALL.txt" % get.srcNAME())


