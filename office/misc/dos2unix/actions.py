#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    for binary in ["dos2unix", "mac2unix", "unix2dos", "unix2mac"]:
        pisitools.dobin(binary)

    pisitools.dodoc("NEWS.txt", "README.txt" ,"TODO.txt", "ChangeLog.txt", "COPYING.txt")
    pisitools.doman("man/man1/dos2unix.1")



