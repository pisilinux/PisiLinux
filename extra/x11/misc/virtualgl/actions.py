# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr/share \
                          -DTJPEG_INCLUDE_DIR=/usr/include \
                          -DTJPEG_LIBRARY=/usr/lib/libturbojpeg.so \
                          -DVGL_LIBDIR=/usr/lib \
                          -DVGL_BINDIR=/usr/bin \
                          -DVGL_INCDIR=/usr/include \
                          -DVGL_DOCDIR=/usr/share/doc/%s" % get.srcNAME(),
                          sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/bin/glxinfo", "/usr/bin/", "vglxinfo")
