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
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-nls  \
                         --prefix=/usr  \
                         --enable-posix  \
                         --with-threads   \
                         --enable-regex    \
                         --with-modules     \
                         --disable-rpath     \
                         --disable-static     \
                         --enable-networking   \
                         --program-suffix=1.8   \
                         --enable-dynamic-linking \
                         --disable-error-on-warning")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.removeDir("/usr/share/info")
    
    pisitools.rename("/usr/share/aclocal/guile.m4", "guile1.8.m4")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "THANKS")
