#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.system("tar xvf opengfx-0.5.1.tar")
    pisitools.insinto("/usr/share/openttd/data/opengfx", "opengfx-0.5.1/*.grf")
    pisitools.insinto("/usr/share/openttd/data/opengfx", "opengfx-0.5.1/*.obg")
    
    pisitools.dodoc("opengfx-0.5.1//changelog.txt", "opengfx-0.5.1//license.txt", "opengfx-0.5.1//readme.txt")
