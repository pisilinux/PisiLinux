#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir ="DSDP%s" % get.srcVERSION()

def build():
    shelltools.export("DSDPROOT", get.curDIR())
    autotools.make("CC=%s LDFLAGS='%s' OPTFLAGS='%s -fPIC'" % (get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    pisitools.dolib("lib/libdsdp.so")
    pisitools.insinto("/usr/include","include/*.h")

    pisitools.dodoc("Readme", "docs/*.pdf")
