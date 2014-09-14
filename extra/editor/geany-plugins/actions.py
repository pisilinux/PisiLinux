#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
	autotools.rawConfigure("--prefix=/usr")
	
	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	pisitools.dodoc("README.waf","README","NEWS")
	autotools.rawInstall("DESTDIR=%s"%get.installDIR())

