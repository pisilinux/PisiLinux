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
    shelltools.export("CFLAGS", "%s -fpie" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

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

    pisitools.dodoc("README.LDAP", "README")
