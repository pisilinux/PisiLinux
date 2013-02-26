#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

#def check():
    #shelltools.cd("harness")
    #pisitools.dodir("testdir")

    #autotools.make("check prefix=../src libdir=../src")


def install():
    autotools.rawInstall("destdir=%s prefix=/ libdir=/lib \
                          includedir=/usr/include usrlibdir=/usr/lib" % get.installDIR())

    pisitools.remove("/usr/lib/libaio.a")

    pisitools.dodoc("ChangeLog", "COPYING", "TODO")
