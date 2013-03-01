#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Documentation/*.*", "/var/local/iptraf", "/var/lib/iptraf")
    pisitools.dosed("Documentation/*.*", "Documentation", "/%s/%s" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make('CC="%s" CFLAGS="%s -DALLOWUSERS" -C src' % (get.CC(), get.CFLAGS()))

def install():
    for f in ["iptraf", "rawtime", "rvnamed"]:
        pisitools.dosbin("src/%s" % f)

    # To allow ordinary users use iptraf, uncomment the following, but it is a security hole
    # pisitools.chmod("/usr/sbin/iptraf", 4755)

    for d in ["lib", "log", "run"]:
        pisitools.dodir("/var/%s/iptraf" % d)

    pisitools.dodoc("LICENSE", "README*", "FAQ", "CHANGES", "RELEASE-NOTES")
    pisitools.doman("Documentation/*.8")
    pisitools.dohtml("Documentation/*")
