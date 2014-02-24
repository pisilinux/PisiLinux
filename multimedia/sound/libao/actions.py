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
    # libtools.libtoolize("--force --install")
    autotools.configure("--disable-dependency-tracking \
                         --enable-alsa \
                         --enable-alsa-mmap \
                         --enable-pulse \
                         --disable-arts \
                         --disable-esd \
                         --disable-nas \
                         --enable-shared \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "CHANGES", "README", "TODO")
