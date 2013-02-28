#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s CFLAGS='%s' IP=/sbin/ip" % (get.CC(), get.CFLAGS()))

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/run/pptp")
    shelltools.chmod("%s/var/run/pptp" % get.installDIR(), 0750)
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "DEVELOPERS",
        "NEWS", "README", "TODO", "USING")

