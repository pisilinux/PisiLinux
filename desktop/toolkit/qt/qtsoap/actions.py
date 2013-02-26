#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    pisitools.dosed("buildlib/buildlib.pro", "\\$\\$DESTDIR", "/usr/lib/")
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("README.TXT", "LICENSE*", "LGPL*")
