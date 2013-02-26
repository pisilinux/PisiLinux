#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "dooble.d/trunk/browser/"

def setup():
	shelltools.system("/usr/bin/qmake -o Makefile dooble.pro")

def build():
	autotools.make()

def install():
	install_dirs = ["Icons","Images","Tab","Dooble"]
	for i in install_dirs:
		pisitools.insinto("/opt/dooble",i)
	pisitools.dobin("dooble.sh")
	pisitools.dodoc("Doc/*")
