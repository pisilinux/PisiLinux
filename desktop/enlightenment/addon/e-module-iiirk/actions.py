#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="iiirk" 

def setup():
    autotools.autoreconf("-vfi")
    shelltools.system("./autogen.sh --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s"% get.installDIR())

    pisitools.dodoc("AUTHORS","COPYING*")
