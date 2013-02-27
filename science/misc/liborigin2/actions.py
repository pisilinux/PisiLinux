#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[1])

def setup():
    shelltools.system('qmake LIBDIR="/usr/lib" BOOSTINC="/usr/include/boost"')

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
