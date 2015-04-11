#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodir("/etc/xdg/qtchooser")
    pisitools.dosym("qt4.conf", "/etc/xdg/qtchooser/default.conf")

    pisitools.dodoc("LICENSE.LGPL", "LGPL_EXCEPTION.txt")
