#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for makefile in ("mk/beforeauto.mk.in", "mk/platforms/i586_linux_2.0_*.mk"):
        pisitools.dosed(makefile, "^CXXDEBUGFLAGS.*", "CXXDEBUGFLAGS = %s" % get.CXXFLAGS())
        pisitools.dosed(makefile, "^CDEBUGFLAGS.*", "CDEBUGFLAGS = %s" % get.CFLAGS())

    for makefile in ("mk/beforeauto.mk.in",
                     "mk/linux.mk",
                     "mk/platforms/i586_linux_2.0_glibc2.1.mk",
                     "src/tool/omniidl/cxx/dir.mk"):
        pisitools.dosed(makefile, "^SharedLibraryPlatformLinkFlagsTemplate = (.*)",
                                  r"SharedLibraryPlatformLinkFlagsTemplate = %s \1" % get.LDFLAGS())

    autotools.configure("--disable-static \
                         --with-openssl=/usr \
                         --with-omniNames-logdir=/var/log/omniNames")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc", "sample.cfg", "omniORB.cfg")
    pisitools.dodir("/var/log/omniNames")
    pisitools.dodir("/var/lib/omniMapper")

    pisitools.dodoc("CREDITS", "COPYING*", "README*")
    pisitools.doman("man/*/*")
