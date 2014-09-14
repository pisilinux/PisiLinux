#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for bin in "mkfs", "fsck":
        pisitools.remove("/sbin/%s.jfs" % bin)
        pisitools.dosym("jfs_%s" % bin, "/sbin/%s.jfs" % bin)

        manfile = "/%s/man8/%s.jfs.8" % (get.manDIR(), bin)

        pisitools.remove(manfile)
        pisitools.dosym("jfs_%s.8" % bin, manfile)

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*", "COPYING")
