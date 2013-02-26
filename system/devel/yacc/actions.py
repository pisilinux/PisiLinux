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

def setup():
    pisitools.dosed("Makefile", " -O ", " $(CFLAGS) ")

def build():
    autotools.make("clean")
    autotools.make('-j1 CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("yacc")

    pisitools.doman("yacc.1")
    pisitools.dodoc("ACKNOWLEDGEMENTS", "NEW_FEATURES", "NOTES", "README*")
