#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ppracer-0.5alpha"

def setup():
    for i in ["src/sqstdlib", "src/squirrel"]:
        if shelltools.isDirectory(i):
            shelltools.unlinkDir(i)

    pisitools.dosed("configure.in", "libpng12", "libpng14")
    autotools.autoreconf("-vfi")

    autotools.configure("--disable-dependency-tracking \
                         --with-data-dir=/usr/share/ppracer \
                         --with-tcl=/usr/lib \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog")

    pisitools.remove("/usr/share/applications/ppracer.desktop")

