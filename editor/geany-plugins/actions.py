#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "geany-plugins-1.22"

def setup():
	autotools.rawConfigure("--prefix=/usr")

def build():
	autotools.make()

def install():
	pisitools.dodoc("README.waf","README","NEWS")
	autotools.rawInstall("DESTDIR=%s"%get.installDIR())

