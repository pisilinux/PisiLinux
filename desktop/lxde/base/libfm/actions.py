#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libfm-%s" % (get.srcVERSION())

def setup():
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --enable-debug \
                         --enable-udisks \
                         --enable-demo")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "TODO")

