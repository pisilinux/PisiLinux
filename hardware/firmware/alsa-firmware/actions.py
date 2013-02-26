#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    pisitools.dosed("configure.in", "multisound/Makefile", "")
    pisitools.dosed("Makefile.am", "multisound", "")

    autotools.autoreconf("-fi")
    autotools.configure("--with-hotplug-dir=/lib/firmware")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #there is no /usr/bin directory (obsoleteman)
    #pisitools.removeDir("/usr/bin")

    # Install additional readme files
    for d in ["hdsploader", "mixartloader", "pcxhrloader", "usx2yloader", "vxloader"]:
        pisitools.newdoc("%s/README" % d, "README.%s" % d)

    pisitools.dodoc("COPYING", "README")
