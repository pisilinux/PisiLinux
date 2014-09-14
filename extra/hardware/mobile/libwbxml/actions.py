#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DLIBWBXML_INCLUDE_DIR=/usr/include \
                          -DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")      
                          
def build():
    shelltools.cd("build")
    cmaketools.make()

def check():
    shelltools.cd("build")
    cmaketools.make("test")

def install():
    shelltools.cd("build")
    cmaketools.install()
