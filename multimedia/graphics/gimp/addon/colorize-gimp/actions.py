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

WorkDir="colorize-gimp"

def setup():
    pisitools.dosed("Makefile", "pardus_cflags", "%s" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CC=.*", "CC=%s" % get.CC())

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "colorize")
