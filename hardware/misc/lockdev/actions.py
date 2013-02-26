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

def setup():
    # disable tests
    pisitools.dosed("Makefile", "^.*cd LockDev && make test$", "")

    # Set CFLAGS
    pisitools.dosed("Makefile", "OPTIMIZE=\".*\"", "OPTIMIZE=\"%s\"" % get.CFLAGS())

def build():
    autotools.make("CC=%s CFLAGS=\"%s -fPIC\"" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("sbindir=%s/sbin \
                          libdir=%s/usr/lib \
                          incdir=%s/usr/include \
                          mandir=%s/usr/share/man" % ((get.installDIR(),)*4))

    pisitools.remove("/usr/lib/*.a")

    pisitools.dosym("liblockdev.so.1.0.3", "/usr/lib/liblockdev.so.1")

    pisitools.dodir("/var/lock/lockdev")
    shelltools.chmod("%s/var/lock/lockdev" % get.installDIR(), 0775)
    shelltools.chown("%s/var/lock/lockdev" % get.installDIR(), "root", "lock")

    # FIXME: This doesnt work
    #shelltools.chmod("%s/sbin/lockdev" % get.installDIR(), mode=02711)
    shelltools.chown("%s/sbin/lockdev" % get.installDIR(), "root", "lock")

    pisitools.dodoc("ChangeLog", "AUTHORS", "LICENSE")
