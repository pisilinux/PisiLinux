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

shelltools.export("HOME", get.workDIR())

# enable loader builds DLL loader for ELF i386 platforms only
dllloader = "--disable-loader " if get.ARCH() == "x86_64" else ""

def setup():
    # Make it build with libtool 1.5
    shelltools.system("rm -rf m4/lt* m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    shelltools.system("./bootstrap")
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("--prefix=/usr \
                            --sysconfdir=/etc \
                            --libdir=/usr/lib \
                            --disable-rpath \
                            --enable-oss \
                            --enable-nls \
                            --enable-pvr \
                            --enable-xosd \
                            --enable-vcdx \
                            --enable-upnp \
                            --enable-opus \
                            --enable-sftp \
                            LUAC=luac5.1 \
                            --enable-aa \
                            --enable-bluray \
                            --enable-a52 \
                            --enable-alsa \
                            --enable-dvbpsi \
                            --enable-dc1394 \
                            --enable-dca \
                            --enable-dv \
                            --enable-dvdnav \
                            --enable-dvdread \
                            --enable-faad \
                            --enable-flac \
                            --enable-freetype \
                            --enable-fribidi \
                            --enable-glx \
                            --enable-gnutls \
                            --enable-libcddb \
                            --enable-libmpeg2 \
                            --enable-libxml2 \
                            --enable-lirc \
                            --enable-live555 \
                            --enable-loader \
                            --enable-lua \
                            --enable-mad \
                            --enable-mkv \
                            --enable-mod \
                            --enable-mpc \
                            --enable-ogg \
                            --enable-png \
                            --enable-projectm \
                            --enable-pulse \
                            --enable-qt4 \
                            --enable-realrtsp \
                            --enable-screen \
                            --enable-sdl \
                            --enable-shared \
                            --enable-skins2 \
                            --enable-smb \
                            --enable-sout \
                            --enable-speex \
                            --enable-svg \
                            --enable-theora \
                            --enable-twolame \
                            --enable-upnp \
                            --enable-vcd \
                            --enable-vcdx \
                            --enable-vlm \
                            --enable-vorbis \
                            --enable-x264 \
                            --enable-xvideo \
                            --enable-v4l2 \
                            --disable-altivec \
                            --disable-bonjour \
                            --disable-gnomevfs \
                            --disable-growl \
                            --disable-jack \
                            --disable-portaudio \
                            --disable-static \
                            --with-x %s " % dllloader )


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    # Fix Firefox plugin location
    # pisitools.domove("/usr/lib/mozilla/plugins/*", "/usr/lib/browser-plugins")
    # pisitools.remove("/usr/lib/browser-plugins/*.la")
    # pisitools.removeDir("/usr/lib/mozilla/")

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "COPYING")

