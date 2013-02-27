#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("dist/Makefile.in", "--optimize 2", "--no-compile")
    autotools.autoconf()
    autotools.configure("--with-apxs=/usr/sbin/apxs")
    pisitools.dosed("src/Makefile","-Wl,--hash-style  $")

def build():
    autotools.make('OPT="`apxs2 -q CFLAGS` -fPIC"')

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
