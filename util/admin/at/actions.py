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
    pisitools.dosed("configure.in", "VERSION=\"3\\.1\\.9\"", "VERSION=\"%s\"" % get.srcVERSION())

    autotools.autoconf("-f")
    autotools.configure("--with-jobdir=/var/spool/at \
                         --with-atspool=/var/spool/at/spool \
                         --with-daemon_username=root \
                         --with-daemon_groupname=root")

def build():
    autotools.make()

def install():
    autotools.rawInstall("IROOT=%s" % get.installDIR())

