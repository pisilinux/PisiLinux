#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("CFLAGS='%s'" % get.CFLAGS())

def install():
    pisitools.doman("irqbalance.1")
    pisitools.dosbin("irqbalance")

    pisitools.dodoc("COPYING", "AUTHORS")
