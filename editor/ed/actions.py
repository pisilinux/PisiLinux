#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure('CC=%s CFLAGS="%s" ' % (get.CC(), get.CFLAGS()))

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
