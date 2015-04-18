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
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    
    options = '--with-package-name="GStreamer for PisiLinux" \
               --with-package-origin="http://www.pisilinux.org" \
               --enable-nls \
               --disable-dependency-tracking \
               --disable-examples \
               --enable-introspection \
               --disable-static \
               --disable-rpath \
               --disable-valgrind \
               --disable-gtk-doc'

    if get.buildTYPE() == "emul32":
        options += " --bindir=/usr/bin32 \
                     --libexecdir=/usr/libexec32 \
                     --disable-introspection"

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.configure(options)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        pisitools.removeDir("/usr/libexec32")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")