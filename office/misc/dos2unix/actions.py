#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    for binary in ["dos2unix", "mac2unix", "unix2dos", "unix2mac"]:
        pisitools.dobin(binary)

    pisitools.dodoc("NEWS.txt", "README.txt" ,"TODO.txt", "ChangeLog.txt", "COPYING.txt")
    pisitools.dohtml("dos2unix.htm")
    pisitools.doman("man/man1/dos2unix.1")



