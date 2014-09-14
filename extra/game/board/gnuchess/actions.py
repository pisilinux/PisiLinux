#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure("--disable-dependency-tracking --enable-readline")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.removeDir("/usr/share/locale/")

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
