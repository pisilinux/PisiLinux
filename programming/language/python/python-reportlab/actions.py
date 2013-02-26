#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    for doc in ["docs/*","demos", "CHANGES.txt", "LICENSE.txt", "README.txt", "VERSION.txt"]:
        pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), doc)

    #Remove bundled fonts
    pisitools.removeDir("/usr/lib/%s/site-packages/reportlab/fonts" % get.curPYTHON())
