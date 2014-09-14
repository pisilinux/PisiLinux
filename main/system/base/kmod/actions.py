#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc \
                         --with-zlib \
                         --with-xz")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.dosym("modprobe.d.5.gz","/usr/share/man/man5/modprobe.conf.5.gz")
    for sym in ["modinfo","insmod","rmmod","depmod","modprobe"]:
        pisitools.dosym("../usr/bin/kmod","/sbin/%s" % sym)
    pisitools.dosym("../usr/bin/kmod","/bin/lsmod")
    pisitools.makedirs("%s/etc/depmod.d" % get.installDIR())
    pisitools.makedirs("%s/etc/modprobe.d" % get.installDIR())
    pisitools.dodoc("NEWS", "README", "TODO", "COPYING")
