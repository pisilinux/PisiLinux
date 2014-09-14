#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.unlink("Makefile")
    autotools.make("newns")

def install():
    pisitools.dodoc("debian/copyright", "debian/changelog", "README")
    pisitools.dobin("os-prober")
    pisitools.dobin("linux-boot-prober")
    pisitools.insinto("/usr/lib/os-prober", "newns")
    pisitools.insinto("/usr/share/os-prober", "common.sh")
    for d in ("os-probes",
              "os-probes/mounted", 
              "os-probes/init",
              "linux-boot-probes",
              "linux-boot-probes/mounted"):
        pisitools.insinto("/usr/lib/%s" % d, "%s/common/*" % d)
        if shelltools.isDirectory("%s/x86" % d):
            pisitools.insinto("/usr/lib/%s" % d, "%s/x86/*" % d)
    shelltools.touch("labels")
    pisitools.insinto("/var/lib/os-prober/", "labels")
