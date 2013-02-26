#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

WorkDir = get.srcDIR().replace("_", "")

def setup():
    pisitools.dosed("makeinclude.in", "^(docdir.*)$", r"\1/html")

    autotools.autoconf()
    autotools.configure("--enable-gl \
                         --enable-shared \
                         --enable-threads \
                         --enable-largefile \
                         --disable-localjpeg \
                         --disable-localzlib \
                         --disable-localpng \
                         --enable-xinerama \
                         --enable-xft \
                         --enable-xdbe \
                         --with-optim='%s' \
                         " % get.CFLAGS())

def build():
    autotools.make()
    autotools.make("-C documentation all")

#def check():
#    shelltools.export("HOME", get.workDIR())

#    autotools.make("check")

def install():
    autotools.install()
    autotools.install("-C documentation")
    autotools.rawInstall("DESTDIR=%s -C fluid" % get.installDIR(), "install-linux")

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")
