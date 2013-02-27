#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcNAME()

def install():
    pisitools.dobin("perlmod")

    pisitools.dodoc("README", "COPYING")
