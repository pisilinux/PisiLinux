#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir="Yarock_%s_source" % get.srcVERSION()

def setup():
    shelltools.system("sed -i '27s/#LIBS/LIBS/' yarock.pro ")
    qt4.configure(parameters="PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("CHANGES", "COPYING")