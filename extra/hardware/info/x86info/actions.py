#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s CFLAGS='%s' LDFLAGS='%s'" % (get.CC(),
                                                       get.CFLAGS(),
                                                       get.LDFLAGS()))

def install():
    pisitools.dosbin("lsmsr")
    pisitools.dosbin("x86info")

    pisitools.doman("x86info.1", "lsmsr.8")

    pisitools.dodoc("COPYING", "README", "TODO")
