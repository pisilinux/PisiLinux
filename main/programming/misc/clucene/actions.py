#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_ASCII_MODE=OFF \
			  -DENABLE_PACKAGING=OFF \
			  -DDISABLE_MULTITHREADING=OFF \
			  -DBUILD_CONTRIBS_LIB:BOOL=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS","README","COPYING","ChangeLog")
