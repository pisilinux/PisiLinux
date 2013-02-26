#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

#shelltools.export("XDG_CACHE_HOME",  get.workDIR())
#shelltools.export("XDG_DATA_HOME",  get.workDIR())
#shelltools.export("GIMP2_DIRECTORY",  get.workDIR())

lines = ["_V = ",
         "_E = echo",
         "INSTALL_DIR=%s/usr/share/openttd/data/opengfx" % get.installDIR(),
         "DOCDIR=%s/usr/share/doc/%s" % (get.installDIR(), get.srcNAME())]

def setup():
    # will not use gimp to regenerate the pngs
    pisitools.dosed('scripts/Makefile.def', 'echo "gimp"', 'echo ""')
    with open("Makefile.local", 'w') as file:
        for line in lines:
            file.write("%s\n" % line)

def build():
    autotools.make()

def install():
    autotools.rawInstall()
#    pisitools.dodir("/usr/share/doc/openttd-opengfx")
#    shelltools.cd("opengfx-%s" % get.srcVERSION())
#    for it in shelltools.ls("*.txt"):
#        pisitools.dosym("/usr/share/openttd/data/opengfx/%s" % it,  "/usr/share/doc/openttd-opengfx/%s" % it)
