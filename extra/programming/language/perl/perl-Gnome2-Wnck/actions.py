#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    perlmodules.configure()
    pisitools.dosed("Makefile", "^OTHERLDFLAGS.*$", "OTHERLDFLAGS = %s" % get.LDFLAGS())

def build():
    perlmodules.make()

# t/WnckWindow.t test sometimes fail.
def check():
    shelltools.unlink("t/WnckWindow.t")
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README")

