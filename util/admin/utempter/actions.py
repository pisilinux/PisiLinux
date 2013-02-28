#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall('RPM_BUILD_ROOT="%s" LIBDIR=/usr/lib' % get.installDIR())
    pisitools.dobin("utmp")
