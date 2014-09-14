#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
