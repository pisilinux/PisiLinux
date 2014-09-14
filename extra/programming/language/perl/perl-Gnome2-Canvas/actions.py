#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()
    pisitools.dosed("Makefile", "^OTHERLDFLAGS.*$", "OTHERLDFLAGS = %s" % get.LDFLAGS())

def build():
    perlmodules.make()

# Tests try to reach root/.config/oxygen-gtk so disable for now.
def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README")

