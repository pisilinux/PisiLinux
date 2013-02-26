#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "."

def build():
    autotools.make("LIB=/lib")

def install():
    autotools.rawInstall("DESTDIR=%s \
                          LIB=/lib \
                          bindir=/sbin \
                          syslibdir=/lib \
                          libmpathdir=/lib/multipath" % get.installDIR())

    pisitools.dodir("/etc/multipath")
    pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("AUTHOR", "COPYING", "FAQ")
