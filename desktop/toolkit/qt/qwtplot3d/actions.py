#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()
    shelltools.cd("doc")
    shelltools.system("doxygen Doxyfile.doxygen")

def install():
    qt4.install()

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
    pisitools.dohtml("doc/web/doxygen/*")

    pisitools.dodoc("COPYING")
