#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools

def build():
    autotools.make("CFLAGS='%s -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s install-bin install-man PREFIX=%s SBINDIR=/sbin" % (get.installDIR(), get.defaultprefixDIR()))
