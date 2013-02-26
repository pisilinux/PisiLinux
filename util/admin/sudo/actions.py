#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fpie" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    #shelltools.unlink("acsite.m4")
    #shelltools.move("aclocal.m4 acinclude.m4")
    autotools.autoreconf("-fi")

    autotools.configure("--libexecdir=/usr/libexec/sudo \
                         --with-noexec=/usr/libexec/sudo/sudo_noexec.so \
                         --with-logging=syslog \
                         --with-logfac=authpriv \
                         --with-pam \
                         --with-pam-login \
                         --with-linux-audit \
                         --with-env-editor \
                         --with-ignore-dot \
                         --with-tty-tickets \
                         --with-ldap \
                         --enable-shell-sets-home \
                         --without-selinux \
                         --without-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # for LDAP
    pisitools.dobin("sudoers2ldif")

    pisitools.domo("tr.po","tr", "sudo.mo")

    pisitools.dodoc("PORTING", "LICENSE", "UPGRADE", "README.LDAP",
                    "README", "TROUBLESHOOTING")
