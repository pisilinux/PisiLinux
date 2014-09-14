#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fomit-frame-pointer", "-ffast-math")

    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-demos \
                         --with-trimesh=opcode \
                         --enable-new-trimesh \
                         --with-drawstuff=X11 \
                         --enable-libccd \
                         --enable-double-precision \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG.txt", "README.txt")
