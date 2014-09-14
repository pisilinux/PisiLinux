#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "openmsx-%s-source" % get.srcVERSION()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/openttd/gm", "openmsx-%s/*.mid" % get.srcVERSION())
    pisitools.insinto("/usr/share/openttd/gm", "openmsx-%s/openmsx.obm" % get.srcVERSION())

    pisitools.dodoc("openmsx-%s/*.txt" % get.srcVERSION())
