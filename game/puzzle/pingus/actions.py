#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

import os

datadir = "/usr/share/pingus"
flags = {"CC": get.CC(), \
         "CXX": get.CXX(), \
         "CCFLAGS": get.CFLAGS(), \
         "CPPFLAGS": get.CXXFLAGS(), \
         "LINKFLAGS": get.LDFLAGS()}


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    scons.make('PREFIX="/usr" \
                CC="%(CC)s" \
                CXX="%(CXX)s" \
                CCFLAGS="%(CCFLAGS)s" \
                CPPFLAGS="%(CPPFLAGS)s" \
                LINKFLAGS="%(LINKFLAGS)s"' % flags)

def install():
    pisitools.dobin("pingus")
    pisitools.dodoc("AUTHORS", "NEWS", "README","TODO")

    pisitools.dodir(datadir)
    shelltools.cd("data/")

    for i in shelltools.ls("./"):
        if not i.startswith("po"):
            pisitools.insinto(datadir, i)

    fixperms("%s/%s" % (get.installDIR(), datadir))

