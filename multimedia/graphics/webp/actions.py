#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#shelltools.export("USER","q")

def setup():
    autotools.configure("--disable-static \
                         --enable-swap-16bit-csp \
                         --enable-experimental \
                         --enable-libwebpmux \
                         --enable-libwebpdemux \
                         --enable-libwebpdecoder \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "PATENTS", "README")
    #shelltools.move("%s/libwebp-0.2.1/doc/*" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())
    #shelltools.move("%s/libwebp-0.2.1/README" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())
