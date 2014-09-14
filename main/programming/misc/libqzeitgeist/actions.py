#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share"]

libsuffix = "-DLIB_SUFFIX=32" if get.buildTYPE() == "emul32" else ""

def setup():
    cmaketools.configure(libsuffix)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    pisitools.dodoc("COPYING", "README")
