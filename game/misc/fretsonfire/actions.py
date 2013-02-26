#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Frets on Fire-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/fretsonfire", "src")
    pisitools.insinto("/usr/share/fretsonfire", "data")

    pisitools.removeDir("/usr/share/fretsonfire/data/win32")

    pisitools.dodoc("copying.txt", "readme.txt", "todo.txt")
