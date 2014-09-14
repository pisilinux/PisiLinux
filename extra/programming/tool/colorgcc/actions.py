#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.dobin("colorgcc")
    pisitools.insinto("/etc", "colorgccrc")

    pisitools.dodir("/usr/share/colorgcc")
    pisitools.dosym("/usr/bin/colorgcc", "/usr/share/colorgcc/colorgcc")

    for c in ["gcc", "cc", "g++", "c++", "gfortran", "gcj", get.CC(), get.CXX()]:
        pisitools.dosym("/usr/share/colorgcc/colorgcc", "/usr/share/colorgcc/%s" % c)

    pisitools.dodoc("COPYING", "ChangeLog", "CREDITS")
