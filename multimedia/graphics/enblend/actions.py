#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "enblend-enfuse-%s-753b534c819d" % get.srcVERSION()

def setup():
    shelltools.system("rm -rf doc")
    autotools.autoreconf("-fi")

    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
