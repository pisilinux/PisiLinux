# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    pisitools.dosed("main.c", "len + 13", "len + 14")

def build():
    autotools.make()

def install():
    pisitools.dobin("btyacc")
    pisitools.newman("manpage", "btyacc.1")
    pisitools.dodoc("README*")
