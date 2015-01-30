#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

cpupower_arch = get.ARCH().replace("i686", "i386")

def build():
    # Build cpupowertools
    shelltools.cd("tools/power/cpupower")
    autotools.make("CPUFREQ_BENCH=false")
    autotools.make("-C debug/%s centrino-decode powernow-k8-decode" % cpupower_arch)

def install():
    # Install cpupowertools stuff
    shelltools.cd("tools/power/cpupower")
    autotools.install("DESTDIR=%s libdir=/usr/lib mandir=/%s CPUFREQ_BENCH=false" % (get.installDIR(), get.manDIR()))

    pisitools.dobin("debug/%s/centrino-decode" % cpupower_arch)
    pisitools.dobin("debug/%s/powernow-k8-decode" % cpupower_arch)