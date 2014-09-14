#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    libtools.libtoolize("--force --install")
    autotools.configure("--disable-doc \
                         --disable-static \
                         --disable-ruby \
                         --disable-csharp \
                         --disable-java \
                         --disable-cxx \
                         --disable-gl \
                         --enable-shared \
                         --enable-ncurses \
                         --enable-slang \
                         --enable-imlib2 \
                         --enable-x11 \
                         --with-x \
                         --x-libraries=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we remove la files but symlinks stay there, so we remove by hand
    pisitools.remove("/usr/lib/*.la")
    #pisitools.removeDir("/usr/share/java")

    pisitools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS","NOTES", "README", "THANKS")
