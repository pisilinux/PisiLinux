#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    autotools.make("V=1")
    


def install():
    pisitools.insinto("/usr/bin", "macfanctld")    
    pisitools.insinto("/etc", "macfanctl.conf")
    pisitools.doman("macfanctld.1")
    
    pisitools.dodoc("README")