#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # Make it build with libtool 1.5
    shelltools.system("rm -rf m4/lt* m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    shelltools.system("./bootstrap")
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("--prefix=/usr \
                            --sysconfdir=/etc \
                            --libdir=/usr/lib \
                            --disable-dependency-tracking \
                            --disable-rpath \
                            --disable-oss \
                            --enable-fast-install \
                            --enable-nls \
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
                            --enable-lua \
                            --enable-mad \
                            --enable-mkv \
                            --enable-mod \
                            --enable-mpc \
                            --enable-ogg \
                            --enable-png \
                            --enable-projectm \
                            --enable-pulse \
                            --enable-realrtsp \
                            --enable-screen \
                            --enable-sdl \
                            --enable-sftp \
                            --enable-shared \
                            --enable-skins2 \
                            --enable-smbclient \
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
                            --disable-static \
                            --disable-update-check \
                            --with-default-font=/usr/share/fonts/dejavu/DejaVuSans.ttf \
                            --with-default-font-family=Sans \
                            --with-default-monospace-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                            --with-default-monospace-font-family=Monospace \
                            --with-x \
                           ")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "COPYING")

