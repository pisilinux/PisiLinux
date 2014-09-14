#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

    pisitools.dodoc("src/CHANGELOG")
