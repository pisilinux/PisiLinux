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

def setup():
    # Forcibly prevent detection of shm_open (which then picks up but
    # does not use -lrt).
    shelltools.system("./buildconf")
    shelltools.export("ac_cv_search_shm_open", "no")


    autotools.configure("--enable-ipv6 \
                         --enable-threads \
                         --with-installbuilddir=/usr/lib/apr-1/build \
                         --with-devrandom=/dev/urandom \
                         --enable-nonportable-atomics \
                         --disable-static")

    # Make it use system's libtool
    pisitools.dosed("build/apr_rules.mk", "\$\(apr_builddir\)\/libtool", "/usr/bin/libtool")
    pisitools.dosed("apr-1-config", "\$\{installbuilddir\}\/libtool", "/usr/bin/libtool")

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Trim exported dependencies
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "-luuid -lcrypt", "")
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), "-luuid -lcrypt", "")

    # Install find_apr.m4
    pisitools.dodir("/usr/share/aclocal")
    pisitools.insinto("/usr/share/aclocal", "build/find_apr.m4")

    pisitools.remove("/usr/lib/apr.exp")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
