#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("--prefix=/usr -DOPENGL_INCLUDE_DIR=/usr/include/GL")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc("README_EN.TXT","README_RU.TXT","CHANGELOG")