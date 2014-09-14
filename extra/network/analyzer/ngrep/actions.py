#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.unlinkDir("pcre-5.0")
    autotools.autoreconf("-fi")

    autotools.configure("--enable-ipv6 \
                         --with-pcap-includes=/usr/include")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["CHANGES", "CREDITS", "README", "REGEX"]:
        pisitools.dodoc("doc/%s.txt" % i)

