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

WorkDir = "psutils"

def build():
    autotools.make("-f Makefile.unix CC='%s' RPM_OPT_FLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
    autotools.make("-f Makefile.unix MANDIR=%s/usr/share/man/man1 DESTDIR=%s install" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("README", "LICENSE")
