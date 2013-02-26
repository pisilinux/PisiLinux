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
    autotools.configure("--enable-shadowgrp \
                         --without-selinux \
                         --with-audit \
                         --with-libpam \
                         --enable-nls \
                         --without-group-name-max-length \
                         --disable-shared")
                         #--with-skey \
def build():
    # Rebuild gmo catalogs
    autotools.make("-C po update-gmo")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    # groups come from coreutils package
    pisitools.remove("/usr/share/man/man1/groups.1")
    pisitools.remove("/bin/groups")

    # Conflicts with man-pages
    pisitools.remove("/usr/share/man/man3/getspnam.3")
    pisitools.remove("/usr/share/man/man5/passwd.5")

    pisitools.dodoc("ChangeLog","README","NEWS")

