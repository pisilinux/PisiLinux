#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

    # Do not link to unused m library
    pisitools.dosed("libtool", "^(postdeps=.*) -lm (.*)$", r"\1 \2")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING.LIB","README")
