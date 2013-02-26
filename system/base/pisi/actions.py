# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    # Install into /usr/lib/pardus so we can protect ourself from python updates
    pythonmodules.install("--install-lib=/usr/lib/pardus")

    pisitools.dosym("pisi-cli", "/usr/bin/pisi")

    pisitools.insinto("/etc/pisi", "pisi.conf-%s" % get.ARCH(), "pisi.conf")
