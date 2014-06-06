#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
    shelltools.cd("build")
    pisitools.dobin("pingus")
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "NEWS", "README","TODO")

    pisitools.dodir(datadir)
    shelltools.cd("data/")

    for i in shelltools.ls("./"):
        if not i.startswith("po"):
            pisitools.insinto(datadir, i)

    fixperms("%s/%s" % (get.installDIR(), datadir))

