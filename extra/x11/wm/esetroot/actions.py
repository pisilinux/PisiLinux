#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    pisitools.cflags.add("-lX11")
    autotools.make()

def install():
    pisitools.insinto("/usr/bin/", "Esetroot")
    pisitools.dodoc("LICENSE")
