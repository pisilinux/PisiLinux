#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-warnings \
                         --enable-8bit-toupper \
                         --enable-externs \
                         --enable-cgi-links \
                         --enable-persistent-cookies \
                         --enable-prettysrc \
                         --enable-source-cache \
                         --enable-charset-choice \
                         --enable-default-colors \
                         --enable-nested-tables \
                         --enable-read-eta \
                         --with-zlib \
                         --enable-nls \
                         --enable-ipv6 \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "AUTHORS", "CHANGES", "COPYING", "INSTALLATION","README")

    pisitools.dobin("lynx")
