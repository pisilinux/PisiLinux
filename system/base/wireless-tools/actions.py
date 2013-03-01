#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CC = .*", "CC = %s" % get.CC())
    pisitools.dosed("Makefile", "^CFLAGS=", "CFLAGS=%s " % get.CFLAGS())

def build():
    autotools.make("BUILD_SHARED=1")

def install():
    autotools.rawInstall("PREFIX=%s/usr \
                          INSTALL_DIR=%s/sbin \
                          INSTALL_LIB=%s/usr/lib \
                          INSTALL_INC=%s/usr/include \
                          INSTALL_MAN=%s/usr/share/man" % ((get.installDIR(),)*5))

    pisitools.dodoc("COPYING", "README")
