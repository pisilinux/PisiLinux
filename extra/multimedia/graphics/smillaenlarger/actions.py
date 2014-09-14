#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="SmillaEnlarger_0.9.0_source"
def setup():
	shelltools.cd("SmillaEnlargerSrc")
	qt4.configure("ImageEnlarger.pro")
def build():
	shelltools.cd("SmillaEnlargerSrc")
	qt4.make()
def install():
	pisitools.dodoc("changelog.txt","gpl-3.0.txt","linux_install.txt","ReadMe.rtf","WhatsNew.rtf")
	shelltools.cd("SmillaEnlargerSrc")
	pisitools.dobin("SmillaEnlarger")
	pisitools.insinto("/usr/share/icons","smilla.png")
