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

WorkDir="STLport-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("build/Makefiles/gmake/gcc.mak", "OPT \+= -O2","OPT +=")
    pisitools.dosed("stlport/stl/_cwchar.h", "_STLP_VENDOR_CSTD::wcsftime", "::wcsftime")

    pisitools.echo("stlport/stl/config/user_config.h", "#define _STLP_NATIVE_INCLUDE_PATH ..")

    autotools.rawConfigure("--prefix=/usr \
                            --with-system-boost \
                            --with-extra-cxxflags=\"%s -fPIC\" \
                            --with-extra-cflags=\"%s -fPIC\" \
                            --with-extra-ldflags=\"%s\"" % (get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

    pisitools.echo("build/Makefiles/config.mak","CFLAGS := %s" % get.CFLAGS())

def build():
    autotools.make("-j1 \
                    -C build/lib \
                    -f gcc.mak \
                    release-shared")

def install():
    autotools.rawInstall("BASE_INSTALL_DIR=%s/usr -C build/lib -f gcc.mak install-release-shared" % get.installDIR())

    pisitools.dodoc("README", "etc/ChangeLog*")
