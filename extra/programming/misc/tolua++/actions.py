#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    scons.make('CC="%s" \
                CCFLAGS="%s" \
                LINK="%s" \
                LINKFLAGS="%s" \
                shared=1 '
                % (get.CC(), get.CFLAGS(), get.CC(), get.LDFLAGS()))

    # Remove static libraries
    shelltools.unlink(get.workDIR()+'/'+get.srcDIR()+'/lib/*.a')

def install():
    for dirs in ["bin", "include", "lib"]:
        pisitools.insinto("/usr", dirs)

    pisitools.dohtml("doc/*")
    pisitools.dodoc("COPYRIGHT", "README*")
