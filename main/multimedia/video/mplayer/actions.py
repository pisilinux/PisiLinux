#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

pisitools.flags.sub("-O[\ds]+", "-O3")

def setup():
#    for f in ["configure", "libmpdemux/demux_rtp.cpp", "libmpdemux/demux_rtp_internal.h"]:
#        pisitools.dosed(f, "([\"<])(liveMedia|BasicUsageEnvironment)(\.hh)([\">])", "\\1\\2/\\2\\3\\4")
#    pisitools.dosed("libmpdemux/demux_rtp.cpp", "GroupsockHelper.hh", "groupsock/GroupsockHelper.hh")
    shelltools.copytree("../ffmpeg-2.2.4", "ffmpeg")
    autotools.rawConfigure(' \
                             --confdir=/usr/share/mplayer \
                             --datadir=/usr/share/mplayer \
                             --prefix=/usr \
                             --charset=UTF-8 \
                             --disable-3dfx \
                             --disable-altivec \
                             --disable-arts \
                             --disable-ass-internal \
                             --disable-bitmap-font \
                             --disable-debug \
                             --disable-dvdread-internal \
                             --disable-esd \
                             --enable-fribidi \
                             --disable-ggi \
                             --disable-libdvdcss-internal \
                             --disable-live \
                             --disable-mga \
                             --disable-nas \
                             --disable-rpath \
                             --disable-svga \
                             --disable-tdfxfb \
                             --disable-tdfxvid \
                             --disable-tga \
                             --disable-tv-v4l1 \
                             --enable-aa \
                             --enable-alsa \
                             --enable-ass \
                             --enable-bl \
                             --enable-bluray \
                             --enable-caca \
                             --enable-cmov \
                             --enable-dvb \
                             --enable-dvdread \
                             --enable-fbdev \
                             --enable-ffmpeg_a \
                             --enable-fontconfig \
                             --enable-freetype \
                             --enable-ftp \
                             --enable-gif \
                             --enable-gl \
                             --enable-gui \
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
                             --enable-radio \
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
                             --enable-theora \
                             --enable-tv \
                             --enable-tv-v4l2 \
                             --enable-unrarexec \
                             --enable-v4l2 \
                             --enable-vdpau \
                             --enable-x11 \
                             --enable-xf86keysym \
                             --enable-xinerama \
                             --enable-xshape \
                             --enable-xv \
                             --enable-xvid \
                             --enable-xvmc \
                             --extra-ldflags="-lvorbisenc -lvorbis -logg" \
                             --extra-libs="-lfribidi -lglib-2.0 -lopenal -ljack -lxvidcore -lfontconfig -lass -laa -lX11 -lXext" \
                             --language=en \
                             --with-xvmclib=XvMCW \
                            ')

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
