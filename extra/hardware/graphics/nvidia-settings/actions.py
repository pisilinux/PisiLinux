#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile", "static", "dynamic")

def build():
    shelltools.cd("src/libXNVCtrl")
    autotools.make('clean')
    autotools.make('CDEBUGFLAGS="-fPIC %s" CC="%s" libXNVCtrl.a' % (get.CFLAGS(), get.CC()))

    shelltools.cd("%s/%s" % (get.workDIR(), get.srcDIR()))
    autotools.make('CC="%s"  LD="%s" STRIP_CMD="/bin/true" NV_VERBOSE=1' % (get.CC(), get.LDFLAGS()))

def install():
    pisitools.dodir("/usr/bin")
    autotools.install("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    #pisitools.insinto("/usr/lib/static", "src/libXNVCtrl/libXNVCtrl.a")
    #pisitools.insinto("/usr/include/NVCtrl", "src/libXNVCtrl/*.h")

    pisitools.dodoc("COPYING", "doc/*.txt")
