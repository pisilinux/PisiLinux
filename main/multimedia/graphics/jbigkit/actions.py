#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="jbigkit"

def build():
    autotools.make("CC=%s CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr libdir=/usr/lib" % get.installDIR())

    pisitools.doman("pbmtools/jbgtopbm.1", "pbmtools/pbmtojbg.1")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "COPYING", "TODO")
