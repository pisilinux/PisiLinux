#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    pisitools.ldflags.add("-z,noexecstack")
    shelltools.cd("build/linux")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", sourceDir="../../source")

def build():
    shelltools.cd("build/linux")
    cmaketools.make()

def install():
    shelltools.cd("build/linux")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/libx265.a")


