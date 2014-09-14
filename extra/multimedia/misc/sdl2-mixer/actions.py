#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "SDL2_mixer-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("timidity/config.h", "/usr/local/lib/timidity", "/usr/share/timidity")
    pisitools.flags.add("-I/usr/include/libmodplug")

    options = "--disable-dependency-tracking \
               --disable-static \
               --enable-music-midi \
               --enable-music-timidity-midi \
               --enable-music-mod \
               --enable-music-mp3 \
               --enable-music-ogg"

    if get.buildTYPE() == "emul32":
        options += " --includedir=/usr/include \
                     --libdir=/usr/lib32"

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES.txt", "COPYING.txt", "README.txt")
