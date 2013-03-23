#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def build():
    pisitools.dosed("Makefile", "^(CFLAGS=)", r"\1%s " % get.CFLAGS())
    pisitools.dosed("Makefile", "^(LDFLAGS=)", r"\1-lX11 -lm ")
    autotools.make()

def install():
    pisitools.dobin("viewer")
    pisitools.rename("/usr/bin/viewer", "hinting")
    pisitools.dodoc("README","COPYING")
