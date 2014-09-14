#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-compression \
                         --enable-remote-debugger \
                         --with-zlib \
                         --enable-gettext \
                         --enable-apache \
                         --enable-wdb \
                         --enable-python \
                         --disable-perl \
                         --disable-ruby \
                         --disable-csharp")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("CS_LICENSE", "LICENSE", "README*")
