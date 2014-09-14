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
    pisitools.insinto("/usr/bin", "gtk-theme-switch2")
    pisitools.insinto("/usr/share/man/man1", "gtk-theme-switch2.1")

    pisitools.dodoc("COPYING", "ChangeLog", "readme")
