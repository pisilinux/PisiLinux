#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pythonmodules.run("setup.py config --prefix=/usr \
                       --docdir=/usr/share/doc/%s" % get.srcNAME())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("docs/*.txt")

