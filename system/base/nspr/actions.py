#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s/mozilla" % (get.srcNAME(), get.srcVERSION())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    # -fno-strict-aliasing workarounds some aliasing violations, see: https://bugzilla.redhat.com/show_bug.cgi?id=487844 -->
    shelltools.system('../nsprpub/configure \
                       --prefix=/usr \
                       --disable-debug \
                       %s \
                       --enable-optimize="%s -fno-strict-aliasing"' % ("--enable-64bit" if get.ARCH() == "x86_64" else "", get.CFLAGS()))

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    # Create nss.pc and nss-config dynamically
    shelltools.system("./generate-pc-config.sh")

    shelltools.cd("build")

    pisitools.insinto("/usr/lib","dist/lib/*.so",sym=False)
    pisitools.insinto("/usr/include/nspr","dist/include/nspr/*.h",sym=False)
    pisitools.insinto("/usr/include/nspr/obsolete","dist/include/nspr/obsolete/*.h",sym=False)
    pisitools.insinto("/usr/include/nspr/private","dist/include/nspr/private/*.h",sym=False)

    # Fix permissions of headers, they're 0640 by default
    shelltools.chmod("%s/usr/include/nspr/*.h" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/include/nspr/*/*.h" % get.installDIR(), 0644)

    pisitools.insinto("/usr/bin","config/nspr-config",sym=False)
    pisitools.insinto("/usr/lib/pkgconfig","config/nspr.pc",sym=False)
