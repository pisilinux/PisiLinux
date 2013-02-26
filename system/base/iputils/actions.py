#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CCOPT='%s -fpie' CC=%s" % (get.CFLAGS(), get.CC()))

    autotools.compile("ifenslave.c -o ifenslave")

def install():
    for app in ["ping", "ping6"]:
        pisitools.dobin(app)

    for app in ["clockdiff", "arping", "rdisc", "tracepath", "tracepath6", "traceroute6", "ifenslave"]:
        pisitools.dosbin(app)

    # We will not need these if we set cap on postInstall like Fedora
    shelltools.chmod("%s/usr/bin/ping" % get.installDIR(), 04711)
    shelltools.chmod("%s/usr/bin/ping6" % get.installDIR(), 04711)

    pisitools.dodoc("RELNOTES")
