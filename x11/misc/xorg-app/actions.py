# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipList = (".", "filelist", "patches", "pisiBuildState")

shelltools.export("HOME", get.workDIR())

def setup():
    # Speed up xkbcomp
    shelltools.export("CFLAGS","%s -DHAVE_STRCASECMP" % get.CFLAGS())

    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        print "Configuring %s..." % package
        shelltools.cd(package)

        if package.startswith(("xcursorgen", "xsm")) or \
                not shelltools.isFile("configure"):
            autotools.autoreconf("-vif")

        autotools.configure("--disable-dependency-tracking \
                             --disable-devel-docs \
                             --with-cpp=/usr/bin/mcpp")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
