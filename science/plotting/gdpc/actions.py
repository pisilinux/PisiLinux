#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "%s -UG_DISABLE_DEPRECATED" % get.CFLAGS())
    shelltools.system("make LDFLAGS=-lm")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "gpl.txt", "*.test")