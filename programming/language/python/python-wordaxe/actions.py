#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s-%s" % (get.srcNAME().split("python-")[1], get.srcVERSION())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("docs/*.pdf", "docs/releasenotes.txt", "docs/license.txt")
