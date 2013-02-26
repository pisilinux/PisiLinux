#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KDIR = kerneltools.getKernelVersion()

def build():
    for i in ["driver/Makefile", "Makefile"]:
        pisitools.dosed(i, "^KVERS \?=.*$", "KVERS ?= %s" % KDIR)

    autotools.make("-C /lib/modules/%s/build M=`pwd`" % KDIR)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/ndiswrapper")

    pisitools.dodoc("README", "AUTHORS", "ChangeLog")
