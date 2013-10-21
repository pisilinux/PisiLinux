#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-static \
                         --enable-gstmix \
                         --disable-schemas-install \
                         --disable-scrollkeeper \
                         --enable-gst-mixer-applet \
                         --enable-pulseaudio \
                         --enable-gstreamer \
                         --with-gnu-ld")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
