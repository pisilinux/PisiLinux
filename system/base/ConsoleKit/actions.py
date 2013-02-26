#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --enable-pam-module \
                         --localstatedir=/var \
                         --with-systemdsystemunitdir=/lib/systemd/system \
                         --with-pid-file=/var/run/ConsoleKit/pid")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/run/ConsoleKit")

    # pam_console-compat
    pisitools.dodir("/var/run/console")

    pisitools.dodoc("AUTHORS","ChangeLog","README", "COPYING", "HACKING", "NEWS", "TODO")
