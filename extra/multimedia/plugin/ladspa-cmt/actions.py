#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cmt"

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CFLAGS())
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/ladspa", "plugins/*.so")
    pisitools.dodoc("README")
    pisitools.dohtml("doc/*")
