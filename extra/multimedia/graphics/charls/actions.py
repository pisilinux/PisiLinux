#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("CharLS.vcproj")
    shelltools.unlink("CharLS.sln")
    cmaketools.configure("-DBUILD_SHARED_LIBS:BOOL=ON \
			  -Dcharls_BUILD_SHARED_LIBS:BOOL=ON \
			  -DCMAKE_BUILD_TYPE:STRING=Release \
			  -DCMAKE_VERBOSE_MAKEFILE=ON \
			  -DBUILD_TESTING=ON \
			  -DCMAKE_INSTALL_PREFIX=/usr")
def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.insinto("/usr/lib/", "libCharLS.so*")

    pisitools.dodoc("License.txt")
