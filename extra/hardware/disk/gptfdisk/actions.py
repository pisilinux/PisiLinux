#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin("cgdisk")
    pisitools.dobin("fixparts")
    pisitools.dobin("gdisk")
    pisitools.dobin("sgdisk")

    pisitools.doman("cgdisk.8")
    pisitools.doman("fixparts.8")
    pisitools.doman("gdisk.8")
    pisitools.doman("sgdisk.8")

    pisitools.dodoc("COPYING", "NEWS", "README")