#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.configure("--enable-amulecmd \
                         --enable-webserver \
                         --enable-amule-daemon \
                         --enable-optimize \
                         --enable-ccache \
                         --enable-alc \
                         --enable-cas \
                         --enable-wxcas \
                         --enable-amule-gui \
                         --enable-alcc \
                         --enable-geoip \
                         --disable-rpath \
                         --disable-debug \
                         --enable-upnp \
                         --with-wxversion=2.8 \
                         --with-wx-config=/usr/bin/wx-config-2.8")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
