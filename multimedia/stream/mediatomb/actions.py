#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #fixing wrong header and library locations for ffmpeg
    pisitools.dosed("configure", "ffmpeg/avformat.h", "libavformat/avformat.h")
    pisitools.dosed("configure.ac", "ffmpeg/avformat.h", "libavformat/avformat.h")
    pisitools.dosed("src/metadata/ffmpeg_handler.cc", "ffmpeg/avformat.h", "libavformat/avformat.h")

    #configuring with ffmpeg
    autotools.configure("--disable-static \
                         --enable-libmagic \
                         --enable-taglib \
                         --enable-curl \
                         --enable-ffmpeg \
                         --with-ffmpeg-h=/usr/include \
                         --with-ffmpeg-libs=/usr/lib")

def build():
    autotools.make()

def install():
    for dirs in ("/var/run/mediatomb", "/var/lib/mediatomb", "/var/log/mediatomb"):
         pisitools.dodir(dirs)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")

