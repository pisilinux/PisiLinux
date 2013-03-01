#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "numpy-%s" % get.srcVERSION()

NUMPY_FCONFIG = "config_fc --fcompiler=gnu95"
f2py_docs = "%s/%s/f2py_docs" % (get.docDIR(), get.srcNAME())

shelltools.export("LDFLAGS", "%s -shared" % get.LDFLAGS())
shelltools.export("ATLAS", "None")
shelltools.export("PTATLAS", "None")

def build():
    pythonmodules.compile(NUMPY_FCONFIG)

def install():
    pythonmodules.install(NUMPY_FCONFIG)

    pisitools.doman("numpy/f2py/f2py.1")

    pisitools.insinto(f2py_docs, "numpy/f2py/docs/*.txt")
    pisitools.dodoc("COMPATIBILITY", "DEV_README.txt", "LICENSE.txt", "THANKS.txt")
