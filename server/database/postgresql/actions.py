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
    autotools.configure("--with-python \
                         --with-perl \
                         --include=/usr/include/postgresql \
                         --with-includes=/usr/include/libxml2/ \
                         --with-tcl \
                         --with-krb5 \
                         --with-openssl \
                         --enable-nls \
                         --with-pam \
                         --with-libxml \
                         --with-libxslt \
                         --with-ldap \
                         --enable-integer-datetimes \
                         --enable-thread-safety \
                         --enable-depend \
                         --host=%s \
                         --libdir=/usr/lib \
                         --disable-rpath \
                         --with-docdir=/usr/share/doc/postgresql" % get.CHOST())

def build():
    if get.LDFLAGS():
        ld = "-j1 LD=%s %s" % (get.LD(), get.LDFLAGS())
    else:
        ld = "-j1 LD=%s" % get.LD()

    autotools.make(ld)

    shelltools.cd("contrib")
    autotools.make(ld)
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.make(ld)
    shelltools.cd("../..")

    shelltools.cd("src/interfaces/libpq")
    autotools.make(ld)
    shelltools.cd("../../..")

    shelltools.cd("doc")
    autotools.make(ld)
    shelltools.cd("..")

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))

    shelltools.cd("contrib")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("../..")

    shelltools.cd("src/interfaces/libpq")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("../../..")

    shelltools.cd("doc")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("..")

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("README", "HISTORY", "COPYRIGHT")
    pisitools.dodoc("doc/MISSING_FEATURES", "doc/KNOWN_BUGS", "doc/TODO", "doc/bug.template")
    pisitools.dodir("/var/lib/postgresql")
    pisitools.dodir("/var/lib/postgresql/data")
    pisitools.dodir("/var/lib/postgresql/backups")
