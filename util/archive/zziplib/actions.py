#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-sdl \
                         --with-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Extract and install shipped man pages
    shelltools.system("tar xvf docs/zziplib-manpages.tar")
    for manp in shelltools.ls("man3"):
        pisitools.doman("man3/%s" % manp)

    pisitools.dohtml("docs/*.htm*")
    pisitools.dodoc("ChangeLog", "COPYING.LIB", "README", "TODO", "docs/COPYING*", "docs/README.SDL")
