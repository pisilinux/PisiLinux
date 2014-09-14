#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import qt4

def build():
    qt4.make("PREFIX=/usr DATADIR=/usr/share SYSCONFDIR=/etc QTDIR=/usr CXX_FLAGS='%s -O3' CC_FLAGS='%s -O3'" % (get.CFLAGS(), get.CXXFLAGS()))

def install():
    qt4.install("PREFIX=/usr DATADIR=/usr/share SYSCONFDIR=/etc QTDIR=/usr DESTDIR=%s" % get.installDIR())
