#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s" % get.srcNAME()

def build():
    autotools.make("-j1")

def install():
    pisitools.dobin("rlplot")
    pisitools.dobin("exprlp")

    pisitools.doman("rlplot.1")
