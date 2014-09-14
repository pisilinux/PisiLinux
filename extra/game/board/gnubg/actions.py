#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "gnubg"

def setup():
	autotools.aclocal("-I m4")
	libtools.libtoolize("--force --copy")
	autotools.autoheader()
	autotools.automake("--add-missing --copy -Wno-portability")
	autotools.autoconf()
	autotools.rawConfigure("--prefix=/usr --enable-threads --disable-dependency-tracking")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("ABOUT-NLS","ChangeLog","CODING","COPYING","NEWS","README","TODO")
	pisitools.dosym("/usr/share/fonts/bitstream-vera","/usr/share/gnubg/fonts/bitstream-vera")
	pisitools.dosym("/usr/share/pixmaps/gnubg-big.png","/usr/share/gnubg/pixmaps/gnubg-big.png")
