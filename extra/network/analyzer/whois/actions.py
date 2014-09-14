#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('OPT="%s" HAVE_LIBIDN=1 HAVE_ICONV=1' % get.CFLAGS())

def install():
    autotools.rawInstall('BASEDIR="%s" prefix=/usr' % get.installDIR())
    pisitools.insinto("/etc/", "whois.conf")

    pisitools.dodoc("README", "COPYING", "debian/changelog")
