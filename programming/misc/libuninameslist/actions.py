# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "libuninameslist"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("COPYING", "LICENSE")
