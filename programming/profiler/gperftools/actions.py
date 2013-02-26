#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # fix for glibc 2.16
    pisitools.dosed("src/base/linuxthreads.cc", "siginfo_t", "siginfo")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --enable-fast-install \
                         --enable-debugalloc \
                         %s" % ("--enable-frame-pointers" if get.ARCH() == "x86_64" else ""))

    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make("noinst_PROGRAMS=' '")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/gperftools" % get.installDIR())

    for f in ["INSTALL", "README_windows.txt"]:
        pisitools.remove("/usr/share/doc/google-perftools/%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
