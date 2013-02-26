#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # Remove bundled gtest and use the system one.
    # acx_pthread.m4 is needed in configure stage, so keep it.
    shelltools.move("gtest", "gtest.bak")
    shelltools.makedirs("gtest/m4")
    shelltools.copy("gtest.bak/m4/acx_pthread.m4", "gtest/m4")
    shelltools.unlinkDir("gtest.bak")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

    # Remove rpath from speexenc and speexdec
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("CHANGES", "COPYING", "CONTRIBUTORS", "README")
