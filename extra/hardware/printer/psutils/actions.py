#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "psutils"

def build():
    autotools.make("-f Makefile.unix CC='%s' RPM_OPT_FLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
    autotools.make("-f Makefile.unix MANDIR=%s/usr/share/man/man1 DESTDIR=%s install" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("README", "LICENSE")
