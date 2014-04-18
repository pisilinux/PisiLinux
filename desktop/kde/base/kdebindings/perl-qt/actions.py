#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde4

def setup():
    kde4.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DCMAKE_SKIP_RPATH=YES \
                    -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    kde4.make()

def install():
    kde4.install()
