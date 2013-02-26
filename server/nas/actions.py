#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("xmkmf")

def build():
    autotools.make("World")

def install():
    if get.buildTYPE() != "emul32":
        autotools.rawInstall("DESTDIR=%s USRLIBDIR=/usr/lib" % get.installDIR())

    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s USRLIBDIR=/usr/lib32 BINDIR=/emul32" % get.installDIR())

    shelltools.chmod("%s/usr/include/audio/*" % get.installDIR(), 0644)

    pisitools.dodoc("FAQ", "HISTORY", "README", "RELEASE", "TODO")
