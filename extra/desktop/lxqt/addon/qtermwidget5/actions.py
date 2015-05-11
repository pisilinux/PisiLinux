# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
		          -DCMAKE_BUILD_TYPE=Release \
		          -DBUILD_DESIGNER_PLUGIN=0 \
		          -DUSE_QT5=true", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib64/*", "usr/lib/")
    pisitools.removeDir("/usr/lib64")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "README", "COPYING")