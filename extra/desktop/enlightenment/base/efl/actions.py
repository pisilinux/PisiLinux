#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get



def setup():
    pisitools.flags.add("-fvisibility=hidden")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --disable-tslib \
                         --disable-systemd \
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
