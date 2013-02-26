#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #prevent sandbox error
    pisitools.dosed("python/aubio/Makefile.in", "^py_compile =.*", "py_compile = /bin/true")

    #workaround for ugly internal libtool, internal libtool strips relative -L options so make them absolute paths
    pisitools.dosed("python/aubio/Makefile.in", "-L\\$\\(top_builddir\\)/ext.*", "-L%s/usr/lib %s/usr/lib/libaubioext.so %s/usr/lib/libaubio.so" % (get.installDIR(), get.installDIR(), get.installDIR()))
    pisitools.dosed("python/aubio/Makefile.in", "-L\\$\\(top_builddir\\)/src.*", "")

    autotools.configure("--disable-static")

def build():
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO")
