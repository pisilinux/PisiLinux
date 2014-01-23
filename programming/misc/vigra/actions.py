#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION())
NoStrip=["/usr/share/doc"]

def setup():
    cmaketools.configure("-DWITH_VIGRANUMPY=1 -DDOXYGEN_FOUND=0")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("README*", "LICENSE*")
