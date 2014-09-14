#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.dodoc("COPYING.txt", "PKG-INFO", "README.txt")

    #Remove .py extensions from scripts in /usr/bin
    for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.domove("/usr/bin/%s" % f, "/usr/bin", f.replace(".py", ""))
