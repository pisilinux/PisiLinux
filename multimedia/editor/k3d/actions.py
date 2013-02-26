#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "k3d-source-0.8.0.1"

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(installPrefix="/usr", sourceDir = "..")

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("PREFIX=%s" % get.installDIR(), "libdir=%s/usr/lib" % get.installDIR())
	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "README")
