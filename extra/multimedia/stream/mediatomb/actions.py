#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #configuring with ffmpeg
    autotools.configure("--disable-static \
                         --enable-libmagic \
                         --enable-taglib \
                         --enable-curl \
                         --enable-ffmpeg \
                         --with-ffmpeg-h=/usr/include \
                         --with-ffmpeg-libs=/usr/lib")

def build():
    autotools.make()

def install():
    for dirs in ("/run/mediatomb", "/var/lib/mediatomb", "/var/log/mediatomb"):
         pisitools.dodir(dirs)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")

