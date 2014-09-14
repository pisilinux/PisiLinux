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
    shelltools.export("CFLAGS","%s -DPROTOTYPES" % get.CFLAGS())

    autotools.configure("--disable-static \
                         --disable-rpath \
                         --with-pic")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README","LICENSE")
