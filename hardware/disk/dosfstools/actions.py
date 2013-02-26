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

WorkDir = "dosfstools-3.0.13"


def build():
    autotools.make("CFLAGS='%s -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s install-bin install-man PREFIX=%s SBINDIR=/sbin" % (get.installDIR(), get.defaultprefixDIR()))

    #pisitools.dodoc("COPYING", "ChangeLog", "doc/*")
