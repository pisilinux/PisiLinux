#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools


WorkDir="kaption-"+get.srcVERSION()
#WorkDir="kaption"


def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` -DCMAKE_BUILD_TYPE=Release")
    #shelltools.system("cmake CMakeLists.txt -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix`")
   

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "TODO", "CHANGELOG", "COPYING")
