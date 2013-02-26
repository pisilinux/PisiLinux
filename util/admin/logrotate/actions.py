#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
