# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
Skip = ("patches", "pisiBuildState", ".")

def setup():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        if package.startswith("xorg-cf-files"):
            pisitools.dosed("host.def", "_PARDUS_CC_", get.CC())
            pisitools.dosed("host.def", "_PARDUS_CXX_", get.CXX())
            pisitools.dosed("host.def", "_PARDUS_AS_", get.AS())
            pisitools.dosed("host.def", "_PARDUS_LD_", get.LD())
            pisitools.dosed("host.def", "_PARDUS_CFLAGS_", get.CFLAGS())
            pisitools.dosed("host.def", "_PARDUS_LDFLAGS_", get.LDFLAGS())

        autotools.configure("--with-config-dir=/usr/share/X11/config")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
