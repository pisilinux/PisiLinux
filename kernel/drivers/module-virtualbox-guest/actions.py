# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("KERN_DIR=/lib/modules/%s/build" % KDIR)
    autotools.make("-C vboxvideo KERN_DIR=/lib/modules/%s/build" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*/*.ko")
