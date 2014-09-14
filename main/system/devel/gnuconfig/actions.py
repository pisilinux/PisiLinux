#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def check():
    autotools.make("check")

def install():
    pisitools.doexe("config.*", "/usr/share/gnuconfig")

    pisitools.dodoc("ChangeLog")
