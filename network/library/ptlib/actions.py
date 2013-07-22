#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED" % get.CFLAGS())

def setup():
    autotools.configure("\
                         --enable-alsa \
                         --enable-audio \
                         --enable-ansi-bool \
                         --enable-atomicity \
                         --enable-configfile \
                         --enable-expat \
                         --enable-httpforms \
                         --enable-ipv6 \
                         --enable-odbc \
                         --enable-openldap \
                         --enable-openssl \
                         --enable-oss \
                         --enable-pipechan \
                         --enable-plugins \
                         --enable-pulse \
                         --enable-resolver \
                         --enable-sdl \
                         --enable-url \
                         --enable-v4l2 \
                         --enable-video \
                         --enable-vidfile \
                         --disable-avc \
                         --disable-appshare \
                         --disable-bsdvideo \
                         --disable-dc \
                         --disable-internalregex \
                         --disable-mlib \
                         --disable-samples \
                         --disable-sunaudio \
                         --disable-v4l \
                         --disable-vfw \
                        ")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # Remove static libraries
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("History.txt", "ReadMe.txt", "ReadMe_QOS.txt", "README_VXWORKS.txt")
