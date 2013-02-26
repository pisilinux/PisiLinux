#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("-j1 CPPOPTS=\"%s\" \
                    XX_LIBS=\"-luniconf -lcrypt\" \
                    WVLINK_CC=%s \
                    LDOPTS=\"%s\" \
                    PREFIX=/usr \
                    BINDIR=/usr/bin \
                    MANDIR=/usr/share/man \
                    PPPDIR=/etc/ppp/peers VERBOSE=1" % (get.CFLAGS(), get.CC(), get.LDFLAGS()))

def install():
    autotools.rawInstall("PREFIX=%s/usr \
                          BINDIR=%s/usr/bin \
                          MANDIR=%s/usr/share/man \
                          PPPDIR=%s/etc/ppp/peers" % ((get.installDIR(),)*4))

    pisitools.dodoc("CHANGES*", "COPYING*", "README*", "TODO", "FAQ")
