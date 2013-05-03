#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    pisitools.dosed("Makefile", "DEFS	=", "DEFS += -DNO_MALLOC_DECL")
    pisitools.dosed("Makefile", "troff -man detex.1l", "nroff -man detex.1l > detex.1")
    pisitools.dosed("Makefile", "LEXLIB	= -ll", "LEXLIB	= -lfl")
    autotools.make()

def install():
    pisitools.dobin("detex")

    pisitools.doman("detex.1l")

    pisitools.dodoc("README", "COPYRIGHT")
