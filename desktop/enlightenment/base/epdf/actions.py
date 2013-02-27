#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("./autogen.sh \
                        --enable-xpdf-headers \
                        --disable-static \
                        --prefix=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "COPYING*", "LICENCE", "README")
