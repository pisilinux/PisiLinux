#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PTHREAD_LIBS", "-lpthread")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gnutls \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "AUTHORS", "LICENSE", "ChangeLog")
