#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    pisitools.dosed("Make.defaults","-O0","-Os")
    autotools.make("libdir=/usr/lib bindir=/usr/bin")

def install():
     autotools.rawInstall("DESTDIR=%s libdir=/usr/lib/" % get.installDIR())
