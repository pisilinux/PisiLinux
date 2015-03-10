#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("KDIR=/lib/modules/%s/build" % KDIR)
    #autotools.make()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib/modules/%s/misc" % KDIR, "bbswitch.ko")

    pisitools.dodoc("NEWS", "README*")
