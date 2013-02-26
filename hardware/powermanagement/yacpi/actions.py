#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "-O2 -Wall -g", get.CFLAGS())
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc/yacpi")

    pisitools.dodoc("CHANGELOG", "COPYING", "README", "THANKS")
