#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"
dbFortify = "dbfile.FORTIFY_SOURCE"

def setup():
    pisitools.dosed("test/Makefile", "^\tcc", "\t%s" % get.CC())
    if shelltools.isFile(dbFortify):
        shelltools.chmod(dbFortify, 0644)

def build():
    autotools.make("-j1")

def check():
    autotools.make("-j1 test")

def install():
    pisitools.dobin("abicheck")
    if shelltools.isFile(dbFortify):
        pisitools.insinto("/usr/share/abicheck/", dbFortify)

    pisitools.doman("abicheck.1")
    pisitools.dodoc("COPYING", "ChangeLog", "INTRO", "README", )
