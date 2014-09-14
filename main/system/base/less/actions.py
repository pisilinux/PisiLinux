#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dobin("less")
    pisitools.dobin("lessecho")
    pisitools.dobin("lesskey")
    pisitools.newman("lesskey.nro", "lesskey.1")
    pisitools.newman("less.nro", "less.1")

    pisitools.dodoc("NEWS", "README", "COPYING")
