#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL2-%s" % get.srcVERSION()
docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -O3" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC -O3" % get.CXXFLAGS())

    # for libtool version matching
    #shelltools.copy("/usr/share/aclocal/ltversion.m4", "acinclude/")
    shelltools.system("./autogen.sh")

    #libtools.libtoolize("--force --copy")

    options = "--enable-sdl-dlopen \
               --disable-arts \
               --disable-esd \
               --disable-nas \
               --enable-pulseaudio-shared \
               --enable-alsa \
               --disable-rpath"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/emul32/bin \
                     --mandir=/emul32/man \
                     "

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.export("CFLAGS", "%s -fPIC -O3 -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -fPIC -O3 -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    libtools.preplib()


    pisitools.dodoc("BUGS.txt", "CREDITS.txt", "COPYING.txt", "README.txt", "README-SDL.txt", "TODO.txt", "WhatsNew.txt")
