#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now"  % get.LDFLAGS())

    pisitools.dosed("Makefile", "gcc (\-Wall.*)", "%s \\1 %s" % (get.CC(), get.CFLAGS()))
    pisitools.dosed("Makefile", "^(LDFLAGS[ \t]+=).*", "\\1 %s" % get.LDFLAGS())

    autotools.make()

def install():
    pisitools.doman("crontab.1", "crontab.5", "cron.8")
    pisitools.dodoc("CHANGES", "CONVERSION", "FEATURES", "MAIL", "README", "THANKS")

    pisitools.dosbin("cron")
    pisitools.dobin("crontab")

    pisitools.dodir("/var/spool/cron/crontabs")
    pisitools.dodir("/etc/cron.d")
