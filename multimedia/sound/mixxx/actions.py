#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "mixxx-%s" % get.srcVERSION()

def build():
    shelltools.export("LINKFLAGS", get.LDFLAGS())
    scons.make("prefix=/usr \
                install_root=%s/usr \
                qtdir=%s \
                djconsole=1 \
                shoutcast=1 \
                optimize=1" % (get.installDIR(), get.qtDIR()))

def install():
    shelltools.export("LINKFLAGS", get.LDFLAGS())
    scons.install("install prefix=/usr \
                   install_root=%s/usr \
                   qtdir=%s \
                   djconsole=1 \
                   shoutcast=1 \
                   optimize=1" % (get.installDIR(), get.qtDIR()))

    pisitools.dodoc("README*", "COPYING", "Mixxx-Manual.pdf")
