# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install("--install-lib=/usr/lib/pardus")

    pisitools.dosym("zorg-cli", "/usr/bin/zorg")

    # This is now provided by xorg-server package.
    pisitools.remove("/usr/share/X11/DriversDB")
