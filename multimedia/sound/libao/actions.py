#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    # libtools.libtoolize("--force --install")
    autotools.configure("--disable-dependency-tracking \
                         --enable-alsa \
                         --enable-alsa-mmap \
                         --enable-pulse \
                         --disable-arts \
                         --disable-esd \
                         --disable-nas \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "CHANGES", "README", "TODO")
