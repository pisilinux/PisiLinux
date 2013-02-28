#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    autotools.make()

def install():
    pisitools.dobin("fdupes")
    pisitools.doman("fdupes.1")
    pisitools.dodoc("CHANGES", "CONTRIBUTORS", "README", "TODO")
