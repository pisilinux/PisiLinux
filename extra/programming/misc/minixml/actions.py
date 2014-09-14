#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DSTROOT=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.removeDir("/usr/share/doc")
    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES", "COPYING", "README")
