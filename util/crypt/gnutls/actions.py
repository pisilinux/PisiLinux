#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    options = "--disable-static \
               --disable-rpath \
               --disable-dependency-tracking \
               --enable-guile \
               --with-zlib \
               --disable-valgrind-tests"

    if get.buildTYPE() == "emul32":
        options += " --disable-hardware-acceleration"

    autotools.configure(options)

def build():
    autotools.make()

def check():
    #some tests fail in emul32
    if get.buildTYPE() == "emul32":
        pass
    else:
        autotools.make("-k check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
