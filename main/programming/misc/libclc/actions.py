#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("svn checkout http://llvm.org/svn/llvm-project/libclc/trunk libclc")
    shelltools.system("svn up -r217247")

    shelltools.cd("libclc")

    shelltools.system("./configure.py --prefix=/usr --pkgconfigdir=/usr/lib/pkgconfig")

def build():
    shelltools.cd("libclc")

    autotools.make()

def install():
    shelltools.cd("libclc")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE.TXT","CREDITS.TXT", "README.TXT")