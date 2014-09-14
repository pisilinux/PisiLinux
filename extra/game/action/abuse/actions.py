#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS", '%s -DEXPDATADIR=\\\"/usr/share/abuse\\\"' % get.CXXFLAGS())
    #pisitools.dosed("src/sdlport/setup.cpp", "/var/games/abuse", "/usr/share/abuse")
    autotools.configure("--datadir=/usr/share/abuse --with-x")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")
