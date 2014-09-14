#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

lines = ["V=1",
         "CXXFLAGS=%s" % get.CXXFLAGS(),
         "LDOPT=%s" % get.LDFLAGS(),
         "STRIP=true",
         "DO_NOT_INSTALL_LICENSE=1",
         "DO_NOT_INSTALL_DOCS=1",
         "DO_NOT_INSTALL_CHANGELOG=1",
         "prefix=/%s" % get.defaultprefixDIR()]

def setup():
    with open("Makefile.local", 'w') as file:
        for line in lines:
            file.write("%s\n" % line)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("changelog.txt", "COPYING", "bundle/docs/*.txt")
