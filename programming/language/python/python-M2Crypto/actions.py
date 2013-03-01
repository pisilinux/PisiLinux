#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "M2Crypto-%s" % get.srcVERSION()
contrib = "%s/%s/contrib" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()
    shelltools.chmod("contrib/*", 0644)

def install():
    pythonmodules.install()

    pisitools.insinto(contrib, "contrib/*")
    pisitools.dohtml("doc/")
