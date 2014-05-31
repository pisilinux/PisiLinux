#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde4

def setup():
    kde4.configure("-DKDE4_BUILD_TESTS=OFF \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DWITH_Qwt5=OFF")

def build():
    kde4.make()

def install():
    kde4.install()
