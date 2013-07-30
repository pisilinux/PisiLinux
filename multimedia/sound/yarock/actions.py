#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("README", "COPYING")