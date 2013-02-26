#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

WorkDir = "jeremysanders-okularplugin-1588330"

def setup():
	cmaketools.configure("--prefix=/usr")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dosym("/usr/lib/libokularplugin.so","/usr/lib/browser-plugins/libokularplugin.so")
	pisitools.dodoc("README")
