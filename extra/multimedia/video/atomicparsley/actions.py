#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.system("./autogen.sh")
	autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dosym("AtomicParsley","/usr/bin/atomicparsley")

    pisitools.dodoc("Changes.txt", "COPYING", "README.md")