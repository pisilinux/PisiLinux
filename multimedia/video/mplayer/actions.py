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
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

#WorkDir = "mplayer"
gcc_version = "4.7.2"
mp_version = "1.1"
ff_version = "1.0"

def fixPermissions(dest):
    for root, dirs, files in os.walk(dest):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixPermissions("DOCS")
    #shelltools.export("LINGUAS", "tr")

    # to keep the source tarball small and avoid sandbox violation from subversion we remove .svn folders
    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define VERSION \\\"SVN-r%s-%s\\\"" > version.h' % (mp_version, gcc_version))
    shelltools.echo("version.sh", 'echo "#define MP_TITLE \\\"%s \\\"VERSION\\\" (C) 2000-2012 MPlayer Team\\n\\\"" >> version.h')
    shelltools.chmod("version.sh", 0755)

    shelltools.export("CFLAGS", "%s -O3" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -O3" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s " % get.LDFLAGS())

    autotools.rawConfigure('--prefix=/usr \
                            --confdir=/usr/share/mplayer \
                            --datadir=/usr/share/mplayer \
                            --enable-gui \
                            --disable-3dfx \
                            --disable-altivec \
                            --disable-arts \
                            --enable-ass-internal \
                            --disable-bitmap-font \
                            --disable-debug \
                            --disable-dvdread-internal \
                            --disable-esd \
                            --disable-fribidi \
                            --disable-ggi \
                            --disable-libdvdcss-internal \
                            --disable-mga \
                            --disable-nas \
                            --disable-ssse3 \
                            --disable-svga \
                            --disable-tdfxfb \
                            --disable-tdfxvid \
                            --enable-aa \
                            --enable-alsa \
                            --enable-ass \
                            --enable-bl \
                            --enable-caca \
                            --enable-cmov \
                            --enable-dvb \
                            --enable-dvdnav \
                            --enable-dvdread \
                            --enable-fbdev \
                            --enable-freetype \
                            --enable-ftp \
                            --enable-gif \
                            --enable-png \
                            --enable-gl \
                            --enable-inet6 \
                            --enable-jack \
                            --enable-joystick \
                            --enable-jpeg \
                            --enable-langinfo \
                            --enable-liblzo \
                            --enable-libopencore_amrnb \
                            --enable-libopencore_amrwb \
                            --enable-libvorbis \
                            --enable-lirc \
                            --enable-mad \
                            --enable-mencoder \
                            --enable-menu \
                            --enable-mmx \
                            --enable-mmxext \
                            --enable-networking \
                            --enable-openal \
                            --enable-ossaudio \
                            --enable-png \
                            --enable-pulse \
                            --enable-radio-v4l2 \
                            --enable-radio-capture \
                            --enable-radio-v4l2 \
                            --enable-real \
                            --enable-rtc \
                            --enable-runtime-cpudetection \
                            --enable-sdl \
                            --enable-shm \
                            --enable-smb \
                            --enable-sse \
                            --enable-sse2 \
                            --enable-tga \
                            --enable-tv \
                            --disable-tv-v4l1 \
                            --enable-tv-v4l2 \
                            --enable-unrarexec \
                            --enable-v4l2 \
                            --disable-vdpau \
                            --enable-x11 \
                            --enable-xf86keysym \
                            --enable-xinerama \
                            --enable-xshape \
                            --enable-xv \
                            --enable-fontconfig \
                            --enable-xvid \
                            --enable-theora \
                            --enable-bluray \
                            --enable-ffmpeg_a \
                            --language=tr \
                            --disable-ass-internal \
                            --enable-xvmc \
                            --with-xvmclib=XvMCW \
                            --charset=UTF-8 \
                            --extra-libs="-lopenal -ljack -lxvidcore -lfontconfig -lass -laa -lX11 -lXext" \
                            --disable-rpath' \
                            )

                            # stuff that fail hede=yes check, but working with hede=auto
                            # do not use: autodetect is fine  --enable-cdparanoia and --enable-libcdio 
                            #  --enable-directfb \
                            #
                            #  not ready 
                            # --enable-live \
                            #
                            #   Maybe used
                            # --disable-ffmpeg_so \

def build():
    autotools.make()

def install():
    autotools.install("prefix=%(D)s/usr \
                       BINDIR=%(D)s/usr/bin \
                       LIBDIR=%(D)s/usr/lib \
                       CONFDIR=%(D)s/usr/share/mplayer \
                       DATADIR=%(D)s/usr/share/mplayer \
                       MANDIR=%(D)s/usr/share/man" % {"D": get.installDIR()})

    # set the default skin for gui
    shelltools.copytree("default_skin", "%s/usr/share/mplayer/skins/default" % get.installDIR())

    # codecs conf, not something user will interact with
    pisitools.insinto("/usr/share/mplayer", "etc/codecs.conf")

    # example dvb conf
    pisitools.insinto("/usr/share/mplayer", "etc/dvb-menu.conf")

    # just for fast access to conf
    pisitools.dosym("/etc/mplayer.conf", "/usr/share/mplayer/mplayer.conf")
    pisitools.dosym("/etc/mencoder.conf", "/usr/share/mplayer/mencoder.conf")

    # install docs, tools, examples
    pisitools.dodoc("AUTHORS", "Changelog", "README", "LICENSE")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "TOOLS")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "DOCS/tech")
    pythonmodules.fixCompiledPy("/usr/share/doc")
