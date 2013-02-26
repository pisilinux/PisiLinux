#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xsys-%s" % get.srcVERSION()

def build():
    autotools.make()

def install():
    pisitools.dolib_so('xsys-2.2.0.so', '/usr/lib/xchat/plugins')

    pisitools.dodoc("ChangeLog","README",)
