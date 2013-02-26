#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

import os

def setup():
    shelltools.export("PATH", "%s:/opt/sun-jdk/bin" % os.environ.get("PATH"))
    shelltools.system("./bootstrap")
    pisitools.dosed("configure", "-ldts" , "-ldca")
    pisitools.dosed("xbmc/utils/SystemInfo.cpp","lsb_release -d","cat /etc/pardus-release")
    autotools.rawConfigure("--disable-ccache \
                            --disable-optimizations \
                            --disable-avahi \
                            --disable-hal \
                            --enable-goom \
                            --enable-gl \
                            --enable-pulse \
                            --enable-ffmpeg-libvorbis \
                            --enable-libbluray \
                            --enable-rtmp \
                            --enable-vdpau \
                            --prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.doman("docs/manpages/*")
    pisitools.dodoc("README","*.txt","LICENSE.GPL")
