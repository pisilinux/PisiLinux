# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())
    options = "--disable-static \
               --enable-xevie \
               --enable-xprint \
               --enable-xinput \
               --enable-xkb \
               --without-doxygen"

    autotools.autoreconf("-vif")
    autotools.configure(options)
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    #pisitools.remove("/usr/include/xcb/xevie.h")
    #pisitools.remove("/usr/include/xcb/xprint.h")

    pisitools.dodoc("COPYING", "NEWS", "README")
