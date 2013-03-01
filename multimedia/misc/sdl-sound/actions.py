#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "SDL_sound-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/libmodplug" % get.CFLAGS())

    for f in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(f)

    autotools.autoreconf("-fi")
    pisitools.dosed("configure", "modplug\.h", "libmodplug/modplug.h")

    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-smpeg \
                         --enable-midi \
                         --enable-flac \
                         --enable-speex \
                         --enable-mikmod \
                         --enable-modplug \
                         --enable-mpglib \
                         --enable-physfs \
                         --enable-ogg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "CREDITS", "README", "TODO")
