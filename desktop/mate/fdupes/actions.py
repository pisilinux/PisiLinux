#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
