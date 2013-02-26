#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "LibVNCServer-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --with-backchannel \
                         --disable-dependency-tracking \
                         --with-24bpp \
                         --with-zlib \
                         --with-jpeg")

    pisitools.dosed("libtool", " -shared ", " -shared -Wl,--as-needed")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/bin/linuxvnc")
