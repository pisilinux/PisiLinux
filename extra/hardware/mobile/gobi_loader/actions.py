#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "-Wall", "-Wall %s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("gobi_loader", "/lib/udev")
    pisitools.insinto("/lib/udev/rules.d", "60-gobi.rules")
    pisitools.dodir("/lib/firmware/gobi")

    pisitools.dodoc("README")
