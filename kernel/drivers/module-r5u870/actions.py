#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
