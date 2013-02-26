#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "nmap-%sDC1" % get.srcVERSION().replace("_", "").upper()

def setup():
    pisitools.dosed("ncat/Makefile.in", "-m 755 -s ncat", "-m 755 ncat")
    autotools.autoconf()
    autotools.configure("--with-openssl \
                         --with-zenmap \
                         --with-ndiff \
                         --with-nping \
                         --with-ncat \
                         --with-liblua")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s STRIP=true" % get.installDIR())
    for i in ["uninstall_zenmap", "nmapfe", "xnmap"]:
        pisitools.remove("/usr/bin/%s" % i)

    pisitools.dodoc("docs/README", "HACKING", "CHANGELOG", "docs/*.txt")
