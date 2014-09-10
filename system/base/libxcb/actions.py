# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-DNDEBUG")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-xevie \
                         --enable-xprint \
                         --enable-xinput \
                         --enable-xkb \
                         --without-doxygen")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "README")
