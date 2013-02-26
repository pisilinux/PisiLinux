#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make('CXXFLAGS="%s"' % get.CXXFLAGS())

def install():
    pisitools.dobin("src/tecnoballz")

    pisitools.insinto("/usr/share/tecnoballz", "src/TecnoballZ/*")
    pisitools.insinto("/var/lib/games/tecnoballz", "tecnoballz.hi")

    pisitools.doman("man/*")
    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README")
