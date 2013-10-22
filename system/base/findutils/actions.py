#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # write sed commands using pisitools.dosed :)
    shelltools.system('sed -i "/^SUBDIRS/s/locate//" Makefile.in')
    shelltools.system('sed -i "/gets is a security hole/d" gnulib/lib/stdio.in.h')

    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())

    autotools.configure("--enable-nls \
                         --without-included-regex \
                         --disable-rpath \
                         --disable-assert \
                         --with-fts \
                         --enable-leaf-optimisation \
                         --enable-d_type-optimization")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
