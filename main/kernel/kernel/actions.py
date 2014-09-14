#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/lib", "/boot"]

shelltools.export("KBUILD_BUILD_USER", "pisilinux")
shelltools.export("KBUILD_BUILD_HOST", "buildfarm")
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

cpupower_arch = get.ARCH().replace("i686", "i386")

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

    # When bumping major version build man files and put them into files/man

    autotools.make("JOBS=5 WERROR=0 -C tools/perf perf HAVE_CPLUS_DEMANGLE=1")

    # Build cpupowertools
    autotools.make("-C tools/power/cpupower CPUFREQ_BENCH=false")
    autotools.make("-C tools/power/cpupower/debug/%s centrino-decode powernow-k8-decode" % cpupower_arch)

def install():
    kerneltools.install()

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    kerneltools.installLibcHeaders()

    # Install cpupowertools stuff
    autotools.install("-C tools/power/cpupower DESTDIR=%s libdir=/usr/lib mandir=/%s CPUFREQ_BENCH=false" % (get.installDIR(), get.manDIR()))

    pisitools.dobin("tools/power/cpupower/debug/%s/centrino-decode" % cpupower_arch)
    pisitools.dobin("tools/power/cpupower/debug/%s/powernow-k8-decode" % cpupower_arch)

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))

    # Build and install the new 'perf' tool
    pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))

