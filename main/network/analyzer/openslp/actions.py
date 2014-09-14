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
    shelltools.export("CFLAGS", "%s -fPIC -fno-strict-aliasing -fPIE -DPIE " % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie -Wl,-z,now" % get.LDFLAGS())
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-rpath \
                         --localstatedir=/var \
                         --enable-slpv1 \
                         --enable-slpv2-security")

def build():
    autotools.make("RPM_OPT_FLAGS='%s'" % get.CFLAGS())

def install():
    autotools.install()
    
    pisitools.dohtml("doc/doc/html/*")
    pisitools.dodoc("AUTHORS", "FAQ", "ChangeLog", "NEWS", "README", "THANKS")
