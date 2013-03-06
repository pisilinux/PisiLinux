#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s -fPIE" LDFLAGS="%s -pie -lgcrypt"' % (get.CC(),
                                                                             get.CFLAGS(),
                                                                             get.LDFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    pisitools.dodir("/run/vpnc")

    pisitools.dodoc("README")
