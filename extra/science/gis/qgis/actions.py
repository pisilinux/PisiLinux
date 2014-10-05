 #!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

#    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
#                          -DSPATIALINDEX_INCLUDE_DIR=/usr/include/libspatialindex \
#                          -DQGIS_MANUAL_SUBDIR=share/man", installPrefix="/usr",sourceDir="..")

    cmaketools.configure("-DWITH_MAPSERVER:BOOL=TRUE \
      -DBINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
      -DENABLE_TESTS:BOOL=OFF \
      -DWITH_INTERNAL_QWTPOLAR:BOOL=TRUE \
      -DWITH_INTERNAL_QEXTSERIALPORT:BOOL=TRUE \
      -DWITH_PYSPATIALITE:BOOL=FALSE \
      -DWITH_TOUCH=TRUE \
      -DQGIS_MANUAL_SUBDIR=share/man", installPrefix="/usr",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("")
    pisitools.dosed('debian/qgis.desktop',  'qgis-icon',  '/usr/share/qgis/images/icons/qgis-icon.png')
    pisitools.insinto("/usr/share/applications/", "debian/qgis.desktop")
    pisitools.domove("/usr/share/qgis/doc/*", "/usr/share/doc/qgis/")
    pisitools.dosym("/usr/share/doc/qgis/news.html", "/usr/share/qgis/doc/news.html")
