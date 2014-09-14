#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

import os

def setup():
    shelltools.export("PATH", "%s:/usr/lib/jvm/java-7-openjdk/bin" % os.environ.get("PATH"))
    shelltools.system("./bootstrap")
    pisitools.dosed("configure", "-ldts" , "-ldca")
    pisitools.dosed("xbmc/utils/SystemInfo.cpp","lsb_release -d","cat /etc/pisilinux-release")
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
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.doman("docs/manpages/*")
    pisitools.dodoc("README","*.txt","LICENSE.GPL")
    
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")