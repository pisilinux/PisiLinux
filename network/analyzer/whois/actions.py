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

def build():
    autotools.make('OPT="%s" HAVE_LIBIDN=1 HAVE_ICONV=1' % get.CFLAGS())

def install():
    autotools.rawInstall('BASEDIR="%s" prefix=/usr' % get.installDIR())
    pisitools.insinto("/etc/", "whois.conf")

    pisitools.dodoc("README", "COPYING", "debian/changelog")
