#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-fi")
    autotools.configure("--disable-dependency-tracking \
                         --with-nss \
                         --with-ldap \
                         --enable-debug \
                         --without-docbook \
                         --disable-rpath")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Move pam module to /lib
    pisitools.domove("/usr/lib/security/pam_pkcs11.so", "/lib/security")

    # Create necessary directories
    pisitools.dodir("/etc/pam_pkcs11/cacerts")
    pisitools.dodir("/etc/pam_pkcs11/crls")

    # Create symlink to /etc/ssl/nssdb
    pisitools.dosym("/etc/ssl/nssdb", "/etc/pam_pkcs11/nssdb")

    # Install conf files
    for f in shelltools.ls("etc/*.conf.example"):
        pisitools.insinto("/etc/pam_pkcs11", f, shelltools.baseName(f).rstrip(".example"))

    pisitools.dodoc("NEWS", "README", "doc/README*")
    pisitools.doman("doc/*.[18]")
