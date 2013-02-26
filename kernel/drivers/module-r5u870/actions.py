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

WorkDir="r5u870_k2.6.27"
KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("KDIR=/lib/modules/%s/build \
                    KVER=%s V=1" % (KDIR, KDIR))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "usbcam/*.ko")
    pisitools.insinto("/lib/firmware", "*.fw")

    pisitools.dodoc("readme", "copying", "ChangeLog", "news")
