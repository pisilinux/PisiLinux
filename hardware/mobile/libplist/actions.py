#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_VERBOSE_MAKEFILE=TRUE \
                          -DPYTHON_EXECUTABLE=/usr/bin/python \
                          -DPYTHON_LIBRARY=/usr/lib/python2.7 \
                          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LESSER", "README")