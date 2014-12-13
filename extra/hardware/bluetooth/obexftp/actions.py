#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                        -DCMAKE_SKIP_RPATH=ON \
                        -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python \
                        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
                        -DCMAKE_INSTALL_LIBDIR=lib \
                        -DENABLE_PERL=YES \
                        -DENABLE_PYTHON=YES \
                        -DENABLE_RUBY=YES \
                        -DENABLE_TCL=YES \
                        -DCMAKE_INSTALL_PREFIX=/usr")
  
def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README","NEWS")