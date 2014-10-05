#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def build():
    autotools.make()


def install():
    shelltools.chmod("*.ttf", 0644)
    pisitools.insinto("usr/share/fonts/serafettin-cartoon/","*.ttf")
    pisitools.dodoc("*.txt")

