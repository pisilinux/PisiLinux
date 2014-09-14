# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# e3 doesn't work when stripped.
NoStrip = ["/"]

def build():
    bits = "64" if get.ARCH() == "x86_64" else "32"
    autotools.make(bits)

def install():
    autotools.rawInstall("PREFIX=%s/usr install" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING.GPL", "COPYRIGHT", "README*")
    pisitools.dohtml("e3.html")
