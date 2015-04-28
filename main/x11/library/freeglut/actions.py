#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "\-DCMAKE_BUILD_TYPE=Release \
              "

    if get.buildTYPE() == "emul32":

        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")

        options += "-DCMAKE_INSTALL_LIBDIR=lib32 \
                   "

    elif get.ARCH() == "x86_64":

        options += "-DCMAKE_INSTALL_LIBDIR=lib \
                   "

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.dohtml("doc/*")
