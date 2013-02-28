#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='xfig.%s' % get.srcVERSION()

def build():
    shelltools.system("xmkmf")
    autotools.make('CC="%s" LOCAL_LDFLAGS="%s" CDEBUGFLAGS="%s" USRLIBDIR=/usr/lib' % (get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    autotools.make('DESTDIR=%s install.all' % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "xfig.png")
    pisitools.removeDir("/etc")
