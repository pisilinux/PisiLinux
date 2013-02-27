#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("Protocol-v2.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
