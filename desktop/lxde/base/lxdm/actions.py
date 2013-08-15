#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile.am", "^(NULL =.*)", r"AUTOMAKE_OPTIONS = subdir-objects\n\1")
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "README", "ChangeLog", "NEWS")
