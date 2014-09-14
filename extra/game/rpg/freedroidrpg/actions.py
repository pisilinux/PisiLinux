#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/usr/share/freedroidrpg"]

def setup():
    shelltools.export("PTHREAD_LIBS", "-lpthread")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-opengl \
                         --enable-editors \
                         --disable-sdltest \
                         --disable-gtktest \
                         --with-x \
                         --with-sdl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Croppy is a standalone program to post-process png files. It crops PNG files to the smallest dimension without losing data. So, we don't need this for game play...
    pisitools.remove("/usr/bin/croppy")

    # Pngtoico takes the FDRPG png files and turns them into Win32 .ico files and then those .ico files get compiled into the Win32 binary. So, we don't need this neither for game play...
    pisitools.remove("/usr/bin/pngtoico")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
