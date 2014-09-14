#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "starfighter-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("makefile", "-O2 -Wall -g","-O3 -Wall -g")
    pisitools.dosed("makefile", "games/parallelrealities/","starfighter/")

def build():
    autotools.make()

def install():
    pisitools.dobin("starfighter")
    pisitools.insinto("/usr/share/starfighter", "starfighter.pak")
    pisitools.dohtml("docs/")
