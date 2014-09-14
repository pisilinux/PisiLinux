#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("2.0_", "2."))

def setup():
    pisitools.dosed("Makefile", '^CFLAGS\?=.*', "CFLAGS=-std=c99 %s" % get.CFLAGS())
    pisitools.dosed("Makefile", '^LDFLAGS\+=.*', "LDFLAGS=$(LIBS) %s" % get.LDFLAGS())

    pisitools.dosed("Makefile", '-L/usr/local/lib', "-L/usr/lib")
    pisitools.dosed("Makefile", '-I/usr/local/include', "-I/usr/include")

def build():
    autotools.make()

def install():
    docDir = os.path.join(get.docDIR(), get.srcNAME())

    pisitools.dobin("xdotool")
    pisitools.dolib("libxdo.so*")

    pisitools.dodoc("CHANGELIST", "COPYRIGHT", "README")
    pisitools.insinto(docDir, "examples")
