#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-ldconfig-at-install \
                         --with-gnu-ld \
                         --disable-test")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "README")
