#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("\
                         --disable-libavcodec-stackalign-hack \
                         --disable-localgsm \
                         --disable-localilbc \
                         --disable-localspeex \
                         --disable-localspeexdsp \
                         --disable-msrp \
                         --disable-samples \
                         --disable-spandsp \
                         --disable-static \
                         --disable-zrtp \
                         --enable-aec \
                         --enable-default-to-full-capabilties \
                         --enable-shared \
                         --enable-versioncheck \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
