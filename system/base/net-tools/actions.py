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
    pisitools.dosed("Makefile", "(?m)^(COPTS =.*)", "COPTS = %s -fPIE" % get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(LOPTS =.*)", "LOPTS = %s -pie" % get.LDFLAGS())

def build():
    shelltools.export("CC", get.CC())

    autotools.make("libdir")
    autotools.make()
    autotools.make("ether-wake")
    autotools.make("i18ndir")

def install():
    autotools.rawInstall("BASEDIR=%s" % get.installDIR())

    pisitools.dosbin("ether-wake")
    pisitools.dosym("/bin/hostname", "/usr/bin/hostname")

    pisitools.dodoc("README", "README.ipv6", "TODO")
