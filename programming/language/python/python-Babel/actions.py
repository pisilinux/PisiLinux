#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "Babel-%s" % get.srcVERSION()

htmltxt = "%s/%s/html" % (get.docDIR(), get.srcNAME())

def build():
    shelltools.system("python setup.py import_cldr")
    #pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dohtml("docs/")
   #pisitools.insinto(htmltxt, "docs/*.txt")
    pisitools.dodoc("LICENSE","AUTHORS","README")
