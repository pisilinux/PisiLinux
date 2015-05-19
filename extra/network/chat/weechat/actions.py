#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_GUILE=OFF \
                          -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
                          -Wno-dev")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS.asciidoc", "ChangeLog.asciidoc", "COPYING", "README.asciidoc")