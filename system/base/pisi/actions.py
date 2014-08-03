# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    pisitools.dosed("pisi/__init__.py", "2.4", "2.6")
    pythonmodules.compile()

def install():
    # Install into /usr/lib/pardus so we can protect ourself from python updates
    pythonmodules.install("--install-lib=/usr/lib/pisilinux")

    pisitools.dosym("pisi-cli", "/usr/bin/pisi")

    shelltools.touch("LOCK")
    shelltools.chmod("LOCK", 0666)
    pisitools.dodir("/run/lock/files.ldb")
    pisitools.insinto("/run/lock/files.ldb", "LOCK")
    pisitools.dodir("/var/lib/pisi/info/files.ldb")
    pisitools.dosym("/run/lock/files.ldb/LOCK", "/var/lib/pisi/info/files.ldb/LOCK")


    pisitools.insinto("/etc/pisi", "pisi.conf-%s" % get.ARCH(), "pisi.conf")

    # we need it teporary
    pisitools.dodir("/usr/lib/pardus")
    pisitools.dosym("/usr/lib/pisilinux/pisi", "/usr/lib/pardus/pisi")
