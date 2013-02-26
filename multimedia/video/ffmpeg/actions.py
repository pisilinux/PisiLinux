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

minimumcpu = "" if get.ARCH() == "x86_64" else "--cpu=atom"


def setup():
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())

    # CPU thing is just used for CMOV detection
    autotools.rawConfigure("--prefix=/usr \
                            %s \
                            --mandir=/usr/share/man \
                            --disable-stripping \
                            --enable-postproc \
                            --enable-gpl \
                            --enable-pthreads \
                            --enable-libtheora \
                            --enable-libvorbis --disable-encoder=vorbis \
                            --enable-libvpx \
                            --enable-x11grab \
                            --enable-runtime-cpudetect \
                            --enable-libdc1394 \
                            --enable-libschroedinger \
                            --enable-librtmp \
                            --enable-libspeex \
                            --enable-libfreetype \
                            --enable-libnut \
                            --enable-libgsm \
                            --enable-libcelt \
                            --enable-libopenjpeg \
                            --enable-frei0r \
                            --enable-libmodplug \
                            --enable-libass \
                            --enable-gnutls \
                            --enable-libcdio \
                            --enable-libpulse \
                            --enable-libv4l2 \
                            --enable-libmp3lame \
                            --enable-libopencore-amrnb \
                            --enable-libopencore-amrwb \
                            --enable-version3 \
                            --enable-libx264 \
                            --enable-libvo-aacenc \
                            --enable-libvo-amrwbenc \
                            --enable-libxvid \
                            --enable-nonfree \
                            --enable-libfaac \
                            --enable-shared \
                            --disable-static \
                            --disable-debug" % minimumcpu)

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")
    pisitools.dodoc("Changelog", "README", "COPYING*")
