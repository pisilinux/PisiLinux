#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    shelltools.system("phpize")
    autotools.configure("--enable-suhosin")

def build():
    autotools.make()

#def check():
#    autotools.make("test")


def install():
    pisitools.insinto("/usr/lib/php/modules","modules/*.so")
    pisitools.dodoc("Changelog", "CREDITS")
