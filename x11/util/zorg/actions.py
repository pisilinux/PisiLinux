# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install("--install-lib=/usr/lib/pardus")

    pisitools.dosym("zorg-cli", "/usr/bin/zorg")

    # This is now provided by xorg-server package.
    pisitools.remove("/usr/share/X11/DriversDB")
