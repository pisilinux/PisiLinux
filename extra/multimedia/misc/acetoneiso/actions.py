#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "acetoneiso_2.3"

def setup():
	shelltools.cd("acetoneiso")
	qt4.configure()

def build():
	shelltools.cd("acetoneiso")
	qt4.make()

def install():
	docs = ["AUTHORS","CHANGELOG","FEATURES","LICENSE","README","TODO"]
	for doc in docs:
		pisitools.dodoc(doc)
	shelltools.cd("acetoneiso")
	qt4.install()
