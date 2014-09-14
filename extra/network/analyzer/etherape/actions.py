#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("AT_M4DIR", "m4")
    shelltools.export("AUTOPOINT", "true")
    # to disable scrollkeeper
    pisitools.dosed("Makefile.am", "src doc glade", "src glade")

    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "NEWS", "OVERVIEW", "README*", "TODO")
