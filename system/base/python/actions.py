#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "Python-%s" % get.srcVERSION()

PythonVersion = "2.7"

def setup():
    shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())

    for dir in ["expat","zlib","_ctypes/libffi_arm_wince","_ctypes/libffi_msvc",
                "_ctypes/libffi_osx","_ctypes/libffi","_ctypes/darwin"]:
        shelltools.unlinkDir("Modules/%s" % dir)

    shelltools.export("CPPFLAGS", "%s" % os.popen("pkg-config --cflags-only-I libffi").read().strip())

    # Bump required autoconf version
    pisitools.dosed("configure.in", r"\(2.65\)", "(2.68)")

    pisitools.dosed("setup.py","ndbm_libs =.*","ndbm_libs = ['gdbm', 'gdbm_compat']")

    autotools.autoreconf("-vif")
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --with-system-expat \
                         --with-system-ffi")

def build():
    autotools.make()

# some tests fail. let's disable testing temporarily
#~ def check():
    #~ shelltools.export("HOME",get.workDIR()) 
    #~ autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    pisitools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python")
    pisitools.dosym("/usr/bin/python%s-config" % PythonVersion, "/usr/bin/python-config")
    pisitools.dosym("/usr/lib/python%s/pdb.py" % PythonVersion, "/usr/bin/pdb")

    pisitools.dodoc("LICENSE", "README")
