#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial = ["libtool"]

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force --copy")
    autotools.configure("--enable-shared \
                         --enable-asm \
                         --enable-gpl \
                         --with-alsa \
                         --with-faad2 \
                         --with-ffmpeg \
                         --with-lame \
                         --with-libdv \
                         --with-libjpeg \
                         --with-libpng \
                         --with-opengl \
                         --with-schroedinger \
                         --with-x \
                         --with-x264 \
                         --without-doxygen \
                         --without-cpuflags")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/libquicktime.la")

    pisitools.dodoc("README", "TODO", "ChangeLog")
