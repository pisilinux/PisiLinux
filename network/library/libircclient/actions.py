#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def setup():
    shelltools.system('./configure --prefix=/usr --localstatedir=/var --enable-shared')

def build():
    autotools.make()

def install():
    pisitools.dodir("usr/lib")
    shelltools.copy("%s/%s/include" % (get.workDIR(),get.srcDIR()),"%s/usr/include" % get.installDIR())
    shelltools.copy("%s/%s/doc" % (get.workDIR(),get.srcDIR()),"%s/usr/share/libircclient" % get.installDIR())
    shelltools.copy("%s/%s/src/libircclient.so" % (get.workDIR(),get.srcDIR()),"%s/usr/lib/libircclient.so" % get.installDIR())
    

