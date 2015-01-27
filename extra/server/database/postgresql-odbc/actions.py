#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "psqlodbc-09.03.0400%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-unixodbc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/lib/psqlodbcw.so", "psqlodbc.so")
    pisitools.remove("/usr/lib/psqlodbcw.la")
    pisitools.dodoc("license.txt", "readme.txt")
