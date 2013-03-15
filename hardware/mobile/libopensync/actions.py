#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed(".", "-Werror", namePattern = "^Makefile.am$", level = 1)

    autotools.autoreconf("-fi")

    autotools.configure("--enable-python --disable-debug --enable-engine --enable-tools")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS")
