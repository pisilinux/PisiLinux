#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

def setup():
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vfi")
    shelltools.cd("mediastreamer2")
    autotools.autoreconf("-vfi")
    shelltools.cd("..")
    autotools.rawConfigure("--enable-shared \
                            --disable-static \
                            --disable-strict \
                            --enable-external-ortp \
                            --enable-nonstandard-gsm \
                            --enable-rsvp \
                            --enable-ssl \
                            --enable-portaudio \
                            --enable-video \
                            --enable-ipv6 \
                            --enable-alsa \
                            --disable-tests \
                            --disable-rpath \
                            --libdir=/usr/lib \
                            --prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gnome")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
