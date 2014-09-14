#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-ssl=openssl \
                         --enable-threadsafe-ssl=posix \
                         --enable-threads=posix \
                         --with-neon \
                         --with-libxml2 \
                         --with-expat")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "FAQ", "COPYING", "NEWS", "README", "TODO", "THANKS")
