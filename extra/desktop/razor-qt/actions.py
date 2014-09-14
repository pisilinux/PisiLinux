#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system(" tar xJvf pisi-azur.tar.xz")
    shelltools.move("pisi-azur", "razorqt-resources/themes/")
    #pisitools.dosed("cmake/RazorLibSuffix.cmake","lib64","lib")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_POLICYKIT=ON \
                          -DBUNDLE_XDG_UTILS=Yes \
                          -DENABLE_LIGHTDM_GREETER=OFF \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DCMAKE_SKIP_RPATH=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
