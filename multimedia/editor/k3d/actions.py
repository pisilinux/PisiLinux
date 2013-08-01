#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    pisitools.flags.add("-DdDOUBLE")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                          -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so", sourceDir = "..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "README")
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
