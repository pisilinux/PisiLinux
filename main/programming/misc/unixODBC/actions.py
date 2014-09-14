#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Use system libtool instead of bundled one
    shelltools.unlinkDir("libltdl")
    libtools.libtoolize("-c -f --ltdl")
    autotools.autoreconf("-fi")

    autotools.configure("--sysconfdir=/etc/unixODBC \
                         --disable-dependency-tracking \
                         --disable-gui \
                         --enable-threads \
                         --enable-drivers \
                         --enable-driver-conf \
                         --disable-stats ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    pisitools.dohtml("doc/*")
