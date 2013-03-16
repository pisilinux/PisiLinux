#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob
import os.path

shelltools.export("LC_ALL", "C")
shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("runtime/Makefile.am", "AUTOMAKE_OPTIONS = cygnus", deleteLine = True)
    autotools.autoreconf("-fi")
    # Static libs should be enabled for mono compiler
    autotools.configure("--enable-parallel-mark \
                         --with-profile4=yes \
                         --disable-system-aot \
                         --with-tls=pthread \
                         --with-jit=yes \
                         --with-sgen=no \
                         --with-libgdiplus=installed \
                         --with-preview=yes \
                         --disable-static \
                         --prefix=/usr \
                         --sysconfdir=/etc \
                         --with-sigalstack=no \
                         --with-moonlight=no \
                         --with-monotouch=no ")

def build():
    shelltools.export("MONO_SHARED_DIR", get.curDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These work on Windows only
    for i in glob.glob("%s/usr/lib/mono/*/Mono.Security.Win32*" % get.installDIR()):
        x = i.split(get.installDIR())[-1]
        if os.path.isdir(x):
            pisitools.removeDir(x)
            continue

        pisitools.remove(x)

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
