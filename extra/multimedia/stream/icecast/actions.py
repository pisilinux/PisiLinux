#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #Fix htmldir
    pisitools.dosed("doc/Makefile.am", "doc/icecast", "doc/icecast/html")
    pisitools.dosed("debian/icecast2.1", "icecast2", "icecast")

    autotools.autoreconf("-vif")
    autotools.configure("--sysconfdir=/etc/icecast \
                         --disable-static \
                         --with-curl \
                         --with-ogg \
                         --with-theora \
                         --with-speex \
                         --enable-yp \
                         --with-openssl=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Create Log Dir
    pisitools.dodir("/var/log/icecast")
    pisitools.dodir("/run/icecast")

    #Correct permissions
    shelltools.chmod("%s/var/log/icecast" % get.installDIR(), 0755 )
    shelltools.chmod("%s/etc/icecast/icecast.xml" % get.installDIR(),  0640)
    shelltools.chmod("%s/run/icecast" % get.installDIR(), 0755)

    pisitools.insinto("/usr/share/pixmaps", "web/icecast.png")

    pisitools.doman("debian/icecast2.1")
