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
    autotools.autoreconf("-vif")
    autotools.configure("--disable-error-on-warning \
                         --disable-static \
                         --enable-posix \
                         --enable-networking \
                         --enable-regex \
                         --enable-nls \
                         --disable-rpath \
                         --with-threads \
                         --with-modules")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    #pisitools.dosed("libtool", *replace)
    #pisitools.dosed("*/libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()

    major = ".".join(get.srcVERSION().split(".")[:2])
    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50guile" % get.installDIR(), 'GUILE_LOAD_PATH="/usr/share/guile/%s"' % major)

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "THANKS")
