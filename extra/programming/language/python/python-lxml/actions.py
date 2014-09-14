#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lxml-%s" % get.srcVERSION()

def build():
    # remove the C extension so that it will be rebuild using the latest Cython
    shelltools.unlink("src/lxml/lxml.etree.c")
    shelltools.unlink("src/lxml/lxml.etree_api.h")
    shelltools.unlink("src/lxml/lxml.objectify.c")

    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),"doc/*")

    pisitools.dodoc("CHANGES.txt", "LICENSES.txt", "TODO.txt")
