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

WorkDir="stk11xx-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("-f Makefile.standalone KVER=%s" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")

    pisitools.dodoc("README")
