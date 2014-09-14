#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --with-libav-extra-configure='--enable-runtime-cpudetect' \
                         --with-package-name='PisiLinux gst-libav package' \
                         --with-package-origin='http://www.pisilinux.org'")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ") 

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README","NEWS","ChangeLog")
