#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="aggdraw-1.2a3-20060212"

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGES","README")
