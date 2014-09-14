#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure('CC="%s" \
                         CXX="%s" \
                         CFLAGS="%s" \
                         CXXFLAGS="%s" \
                         LDFLAGS="%s"' % (get.CC(), get.CXX(), get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR="%s" install-man' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
