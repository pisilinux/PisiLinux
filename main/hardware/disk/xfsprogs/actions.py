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
    shelltools.export("OPTIMIZER", "%s" % get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--enable-readline=yes \
                         --enable-blkid=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR())
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-dev")
    # Needed for building the QA testsuite
    #autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-qa")

    # Nuke static libraries
    pisitools.remove("/lib/libhandle.a")
    pisitools.remove("/lib/libhandle.la")
    pisitools.remove("/usr/lib/*.a")

    # Fix the symlink
    pisitools.remove("/usr/lib/libhandle.so")
    pisitools.dosym("/lib/libhandle.so.1", "/usr/lib/libhandle.so")

    # Set +x bit for the library
    shelltools.chmod("%s/lib/libhandle.so.*.*.*" % get.installDIR(), 0755)
