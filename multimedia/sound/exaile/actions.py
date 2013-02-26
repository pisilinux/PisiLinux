#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
	autotools.make()

def install():
	autotools.rawInstall("PREFIX=/usr DESTDIR=%s"%get.installDIR())
	pisitools.dodoc("COPYING","INSTALL","README","DEPS","FUTURE")

