#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "gfan0.4plus"

def build():
    autotools.make()

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin" % get.installDIR())

    pisitools.dodoc("doc/*","COPYING", "README", "LICENSE")
