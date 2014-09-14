#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "poster-20060221"

def build():
    shelltools.system("%s %s %s poster.c -lm -o poster" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("poster")

    pisitools.dodoc("README")
    pisitools.doman("poster.1")
