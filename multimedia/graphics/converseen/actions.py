#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure()
    
def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("COPYING", "INSTALL", "README*")
