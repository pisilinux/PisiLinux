#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    cmaketools.make()

def install():
    pisitools.insinto("/usr/bin", "dist/*/bin/*")
    pisitools.insinto("/usr/include", "dist/*/include/*")
    pisitools.insinto("/usr/lib", "dist/*/lib/*")
    pisitools.insinto("/usr/lib", "dist/*/python/*")
    pisitools.insinto("/usr/share/doc", "dist/*/doc*")
    
    pisitools.dodoc("CREDITS", "LICENSE", "README.*")
