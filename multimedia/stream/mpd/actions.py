#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

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
                         --enable-lastfm \
                         --enable-bzip2 \
                         --enable-iso9660 \
                         --enable-mms \
                         --enable-cue \
                         --enable-curl")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
