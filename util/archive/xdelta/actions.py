#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

def build():
    autotools.make('CFLAGS="%s `pkg-config glib-2.0 --cflags`"' % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

