#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Forcibly prevent detection of shm_open (which then picks up but
    # does not use -lrt).
    shelltools.system("./buildconf")
    shelltools.export("ac_cv_search_shm_open", "no")

    autotools.configure("--disable-static \
                         --includedir=/usr/include/apr-1 \
                         --with-installbuilddir=/usr/lib/apr-1/build \
                         --with-devrandom=/dev/urandom \
                         --enable-nonportable-atomics --without-sendfile")

    # Make it use system's libtool
    pisitools.dosed("build/apr_rules.mk", "\$\(apr_builddir\)\/libtool", "/usr/bin/libtool")
    pisitools.dosed("apr-1-config", "\$\{installbuilddir\}\/libtool", "/usr/bin/libtool")
    
    # fix unused-direct-shlib-dependency
    pisitools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Trim exported dependencies
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "-luuid -lcrypt", "")
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), "-luuid -lcrypt", "")

    # Install find_apr.m4
    pisitools.dodir("/usr/share/aclocal")
    pisitools.insinto("/usr/share/aclocal", "build/find_apr.m4")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
