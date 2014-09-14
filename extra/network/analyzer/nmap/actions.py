#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

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
