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
    shelltools.cd("autoconf")
    autotools.autoconf()
    autotools.autoheader()

    for i in ["configure", "defs.h.in"]:
        if shelltools.isFile("../%s" % i):
            shelltools.unlink("../%s" % i)
        shelltools.copy(i, "../")

    shelltools.cd("..")
    autotools.configure('--libdir="/lib" CFLAGS="%s -fPIC"' % get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("INSTALL", "README*")
