#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())


def setup():
    cmaketools.configure("-DWANT_SVN_STAMP=OFF \
                          -DWANT_GIT_STAMP=0 \
                          -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Documentations
    shelltools.cd("docs")
    pisitools.dodoc("AUTHORS*", "CHANGELOG*", "COPYRIGHT*", "gnu_gpl_3.0.txt", "README*")