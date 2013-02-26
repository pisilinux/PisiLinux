# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.remove("/usr/include/xcb/xevie.h")
    #pisitools.remove("/usr/include/xcb/xprint.h")

    pisitools.dodoc("COPYING", "NEWS", "README")
