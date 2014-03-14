#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/fdl.texi", "@appendixsubsec", "@appendixsec")
    autotools.autoreconf("-vfi")
    shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    autotools.configure("--disable-static \
                         --without-ibmtts \
                         --without-nas \
                         --without-flite \
                         --with-alsa \
                         --with-espeak \
                         --with-libao \
                         --with-pulse")

def build():
    autotools.make()

def install():
    autotools.install()

    # Remove redundant conf files
    pisitools.removeDir("/usr/share/opentts")

    pisitools.dodoc("AUTHORS", "COPYING", "README")   
    
    pisitools.remove("/usr/lib/libdumbtts.so")
    pisitools.remove("/usr/lib/libdumbtts.so.0")