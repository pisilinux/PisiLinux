#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "pyblock-0.47-1_20100712"

def build():
    shelltools.export("CFLAGS", "%s -g -I/usr/include/%s -Wall -Werror -fPIC" % (get.CFLAGS(), get.curPYTHON()))
    shelltools.export("LDFLAGS", "%s -shared" % get.LDFLAGS())
    autotools.make("USESELINUX=0")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
