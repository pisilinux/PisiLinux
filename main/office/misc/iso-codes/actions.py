#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domove("/usr/share/pkgconfig/iso-codes.pc","/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/share/pkgconfig")

    pisitools.dodoc("ChangeLog","LICENSE", "README", "TODO")
