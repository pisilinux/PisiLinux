#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	#Not sure but it is not needed (obsoleteman)
    #autotools.autoreconf("-fiv")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING")

