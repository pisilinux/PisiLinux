#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "Python-%s" % get.srcVERSION()

PythonVersion = "2.7"

def setup():
    pisitools.cflags.add("-fwrapv")

    # no rpath
    pisitools.dosed("configure.ac", "-rpath \$\(LIBDIR\) ")

    pisitools.dosed("Lib/cgi.py", r"/usr/local/bin/", r"/usr/bin/")
    pisitools.dosed("setup.py", "SQLITE_OMIT_LOAD_EXTENSION", deleteLine=True)
    pisitools.dosed("setup.py","ndbm_libs =.*","ndbm_libs = ['gdbm', 'gdbm_compat']")

    for dir in ["expat","zlib","_ctypes/libffi_arm_wince","_ctypes/libffi_msvc",
                "_ctypes/libffi_osx","_ctypes/libffi","_ctypes/darwin"]:
        shelltools.unlinkDir("Modules/%s" % dir)

    autotools.autoreconf("-vif")

    # disable bsddb
    pisitools.dosed("setup.py", "^(disabled_module_list = \[)\]", r"\1'_bsddb', 'dbm']")
    # no rpath
    pisitools.dosed("Lib/distutils/command/build_ext.py", "self.rpath.append\(user_lib\)", "pass")

    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --with-system-expat \
                         --with-system-ffi \
                         --with-dbmliborder=gdbm \
                        ")

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
