#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="weather"

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    shelltools.system("./autogen.sh")

def build():
    autotools.make()

def install():
    pisitools.dodoc("AUTHORS", "COPYING*", "README")
