#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-ldconfig-at-install \
                         --with-gnu-ld \
                         --disable-test")


def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPY*", "NEWS", "README")
    pisitools.dodoc("doc/*")
    pisitools.remove("/usr/share/doc/libisofs/doxygen.conf*")
