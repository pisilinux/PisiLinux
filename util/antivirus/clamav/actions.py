#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-id-check \
                         --disable-clamav \
                         --disable-zlib-vcheck \
                         --with-tcpwrappers \
                         --disable-experimental \
                         --with-dbdir=/var/lib/clamav")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/run/clamav")
    pisitools.dodir("/var/log/clamav")

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING*", "NEWS", "README", "ChangeLog", "FAQ")
