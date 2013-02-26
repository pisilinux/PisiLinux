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

WorkDir = "tevent-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    # Create symlinks for so file
    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so.%s" % get.srcVERSION().split(".")[0])
    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so")
