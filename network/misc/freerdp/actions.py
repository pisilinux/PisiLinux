#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_LIBDIR=lib")

def build():
    cmaketools.make()

def check():
    pass

def install():
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    cmaketools.install()
    
    pisitools.dodoc("LICENSE", "README", )
