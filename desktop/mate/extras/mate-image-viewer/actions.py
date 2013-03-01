#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("LDFLAGS", "%s -lgmodule-2.0" % get.LDFLAGS())
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --enable-introspection=yes \
				    --disable-schemas-compile \
				    --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
