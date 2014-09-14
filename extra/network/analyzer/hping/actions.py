#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "hping3-20051105"

def setup():
    pisitools.dosed("Makefile.in", "^CC=.*", "CC = %s" % get.CC())
    for i in ["ar", "ranlib"]:
        pisitools.dosed("Makefile.in", "/usr/bin/%s" % i, i)

    autotools.configure("--force-libpcap")

def build():
    autotools.make()

def install():
    pisitools.dosbin("hping3")
    for i in ["", "2"]:
        pisitools.dosym("hping3", "/usr/sbin/hping%s" % i)

    pisitools.doman("docs/hping3.8")
    pisitools.dodoc("NEWS", "README", "TODO", "AUTHORS", "BUGS", "CHANGES")
