#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "arado-0.2.1/trunk"

def setup():
        autotools.rawConfigure('--prefix=/usr --distro=PisiLinux')

def build():
        autotools.make()

def install():
        pisitools.dobin('bin/arado')
        pisitools.dodoc('doc/*')
        pisitools.dodoc('helpfiles/*')
        pisitools.insinto('/usr/share/pixmaps','images/arado-logo-coloured.png')
        pisitools.insinto('/usr/share/arado','*')
