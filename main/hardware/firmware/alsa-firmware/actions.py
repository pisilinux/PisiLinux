#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    pisitools.dosed("configure.ac", "multisound/Makefile", "")
    pisitools.dosed("Makefile.am", "multisound", "")

    autotools.autoreconf("-fi")
    autotools.configure("--with-hotplug-dir=/lib/firmware")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove conflicted file, it is in linux-firmware package
    pisitools.remove("lib/firmware/ctefx.bin")

    # Install additional readme files
    for d in ["hdsploader", "mixartloader", "pcxhrloader", "usx2yloader", "vxloader"]:
        pisitools.newdoc("%s/README" % d, "README.%s" % d)

    pisitools.dodoc("COPYING", "README")
