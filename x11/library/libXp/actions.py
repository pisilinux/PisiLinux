# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
#    autotools.autoreconf("-vif")

    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.rename("/usr/lib32/libXp.so", "libdeprecatedXp.so")
        return

    # This library is deprecated. Make its usage hard.
    pisitools.rename("/usr/lib/libXp.so", "libdeprecatedXp.so")
    pisitools.removeDir("/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/share")
