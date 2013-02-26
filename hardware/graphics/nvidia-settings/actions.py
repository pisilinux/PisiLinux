#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "static", "dynamic")

def build():
    shelltools.cd("src/libXNVCtrl")
    autotools.make('CDEBUGFLAGS="-fPIC %s" CC="%s" libXNVCtrl.a' % (get.CFLAGS(), get.CC()))

    shelltools.cd("%s/%s" % (get.workDIR(), get.srcDIR()))
    autotools.make('CC="%s" STRIP_CMD="/bin/true"' % get.CC())

def install():
    pisitools.dodir("/usr/bin")
    autotools.install("ROOT=%s" % get.installDIR())

    #pisitools.insinto("src/libXNVCtrl/libXNVCtrl.a" , "/usr/lib/static")
    #pisitools.insinto("src/libXNVCtrl/NVCtrl.h" , "/usr/include/NVCtrl")
    #pisitools.insinto("src/libXNVCtrl/NVCtrlLib.h" , "/usr/include/NVCtrl")

    pisitools.dodoc("COPYING", "doc/*.txt")
