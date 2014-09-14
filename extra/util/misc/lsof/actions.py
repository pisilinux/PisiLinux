#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "lsof_%s_src" % get.srcVERSION()

def setup():
    shelltools.export("LINUX_BASE", "/proc")
    shelltools.export("LSOF_LDFLAGS", get.LDFLAGS())

    shelltools.touch(".neverInv")
    shelltools.system("./Configure -n linux")

def build():
    autotools.make('CC="%s" DEBUG="%s" all' % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dosbin("lsof")

    pisitools.insinto("/usr/share/lsof/scripts", "scripts/*")

    pisitools.doman("lsof.8")
    pisitools.dodoc("00*")
