#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile", "^CC.*", "CC = %s" % get.CC())
    #pisitools.dosed("doc/Makefile", "xmlto", "xmlto --skip-validation")
    pisitools.dosed("gfxboot-font.c", "#include <freetype/ftsynth.h>", "#include <freetype2/ftsynth.h>")


def build():
    autotools.make()
    autotools.make("-j1 doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make('DESTDIR="%s" installsrc' % get.installDIR())

    pisitools.dodoc("doc/*.txt", "doc/*.html")
