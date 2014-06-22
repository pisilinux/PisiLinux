#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    #autotools.autoreconf("-fiv")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-id-check \
                         --disable-clamav \
                         --disable-zlib-vcheck \
                         --with-tcpwrappers \
                         --disable-experimental \
                         --with-dbdir=/var/lib/clamav")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/run/clamav")
    pisitools.dodir("/var/lib/clamav")
    pisitools.dodir("/var/log/clamav")
    shelltools.touch(get.installDIR() + "/var/log/clamav/freshclam.log")
    shelltools.chmod(get.installDIR() + "/var/log/clamav/freshclam.log", 0600)
    shelltools.chown("%s/var/log/clamav/freshclam.log" % get.installDIR(), "clamav", "clamav")

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING*", "NEWS", "README", "ChangeLog", "FAQ")
