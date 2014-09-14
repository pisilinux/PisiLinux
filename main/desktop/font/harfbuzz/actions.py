#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--with-glib=yes \
               --with-freetype=yes \
               --with-cairo=yes \
               --with-icu=yes \
               --with-gobject=yes \
               --with-graphite2=yes"

    if get.buildTYPE() == "emul32":
        options += "--with-glib=yes \
                    --with-graphite2=no \
                    --with-cairo=yes \
                    --with-icu=yes"
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
