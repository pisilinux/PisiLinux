#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    pisitools.dosed("po/Makefile.*", "@MKINSTALLDIRS@", "%s/mkinstalldirs" % get.curDIR())

    autotools.configure("--disable-gdkpixbuf-plugin \
                         --disable-infinite \
                         --disable-jack \
                         --disable-esd \
                         --disable-rpath \
                         --enable-extra-optimization")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README", "AUTHORS")
