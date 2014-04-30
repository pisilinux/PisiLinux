#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --disable-silent-rules \
                         --disable-tslib \
                         --disable-physics \
                         --enable-xine \
                         --enable-fb \
                         --enable-doc \
                         --enable-xinput22 \
                         --enable-multisense \
                         --enable-image-loader-webp \
                         --enable-harfbuzz")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("-j1 doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")