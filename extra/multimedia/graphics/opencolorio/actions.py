# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DOCIO_BUILD_APPS=ON \
                          -DOCIO_BUILD_STATIC=OFF \
                          -DUSE_EXTERNAL_TINYXML=ON \
                          -DOCIO_USE_BOOST_PTR=ON \
                          -DUSE_EXTERNAL_YAML=OFF \
                          -DUSE_EXTERNAL_LCMS=TRUE \
                          -DOCIO_BUILD_PYGLUE=ON \
                          -DOCIO_USE_SSE=OFF \
                          -DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")


def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
