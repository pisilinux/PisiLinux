#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-shared \
                         --disable-threads \
                         --enable-unicode \
                         --with-system-gmp \
                         --disable-rpath \
                         --enable-boehm=system \
                         --with-clx")

    # ecl is installing some files direcly under /usr/share/doc directory wich is not normal.
    pisitools.dosed("build/doc/Makefile", 'doc/\$\{PACKAGE_TARNAME\}', 'doc/ecl')


def build():
    # ecl has parallel make problems, bug reported upstream. (ecls-Bugs-2823867)
    autotools.make("-j1")

def install():
    autotools.install()

    # If these are needed just remove the line below
    pisitools.remove("/usr/lib/ecl-11.1.1/*.a")

    pisitools.dodoc("src/CHANGELOG")
