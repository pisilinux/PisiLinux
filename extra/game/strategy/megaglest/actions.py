#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DWANT_SVN_STAMP=OFF \
                          -DWANT_GIT_STAMP=OFF \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr" ,sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()

    # Documentations
    shelltools.cd("..")
    shelltools.cd("docs")
    pisitools.dodoc("AUTHORS*", "CHANGELOG*", "COPYRIGHT*", "gnu_gpl_3.0.txt", "README*")