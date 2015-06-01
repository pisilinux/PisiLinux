# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipFiles = [".pc", "filelist", "patches", "pisiBuildState"]

def setup():
    #pisitools.dosed("*/Makefile.am", r"/doc/\$\(PACKAGE\)", "/doc/xorg-proto")

    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        autotools.autoreconf("-vif")
        autotools.configure("--without-xmlto \
	                     --without-fop \
	                     --libexecdir=/usr/lib")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
