#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--enable-pulse \
                         --enable-ao \
                         --enable-alsa \
                         --enable-lsr \
                         --enable-jack \
                         --enable-lame-encoder \
                         --enable-vorbis-encoder \
                         --enable-httpd-output \
                         --with-zeroconf=avahi \
                         --enable-shout \
                         --enable-sndfile \
                         --disable-mpc \
                         --enable-bzip2 \
                         --enable-iso9660 \
                         --disable-systemd-daemon \
                         --enable-mms \
                         --enable-curl")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")