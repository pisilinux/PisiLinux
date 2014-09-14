#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4

def setup():
    #shelltools.system("git pull origin master")
    kde4.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DCMAKE_BUILD_TYPE=Release")

def build():
    kde4.make()

def install():
    kde4.install()

    #pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
