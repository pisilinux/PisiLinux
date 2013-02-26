#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-ssl=gnutls --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/doc/%s/examples"% get.srcTAG(), "doc/*.example")
    pisitools.insinto("/usr/share/doc/%s/examples"% get.srcTAG(), "scripts/msmtpqueue/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "doc/Mutt+msmtp.txt")
