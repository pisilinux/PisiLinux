#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "."))
shelltools.export("HOME", get.workDIR())

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/fonts/liberation-fonts", "*ttf*/*.ttf")
    pisitools.dosym("../conf.avail/59-liberation-fonts.conf", "/etc/fonts/conf.d/59-liberation-fonts.conf")

    pisitools.dodoc("COPYING", "*.txt", "AUTHORS", "ChangeLog", "README")
