#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\" WITH_ACL=yes" % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s MANDIR=%s" % (get.installDIR(), get.manDIR()))

    pisitools.dodir("/etc/logrotate.d")

    pisitools.dobin("examples/logrotate.cron", "/etc/cron.daily")
    pisitools.insinto("/etc", "examples/logrotate-default", "logrotate.conf")

    pisitools.dodoc("CHANGES", "COPYING", "README*")
