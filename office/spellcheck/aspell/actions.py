#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.configure("--disable-static \
                         --sysconfdir=/etc/aspell \
                         --enable-docdir=/usr/share/doc/%s" % get.srcNAME())

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install ispell/spell compatibility scripts
    pisitools.insinto("/usr/bin","scripts/ispell","ispell-aspell")
    pisitools.insinto("/usr/bin","scripts/spell", "spell-aspell")

    pisitools.dodoc("README*", "TODO")
