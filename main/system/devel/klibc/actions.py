#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

import os

WorkDir = "klibc-%s" % get.srcVERSION()
NoStrip = "/"
KDIR = kerneltools.getKernelVersion()
klibcarch = "x86_64" if get.ARCH() == "x86_64" else "i386"

docs = {"usr/klibc/arch/README.klibc.arch": "README.arch",
        "usr/dash/README.dash": "README.dash",
        "usr/dash/TOUR": "TOUR.dash",
        "usr/gzip/README": "README.gzip",
        "usr/gzip/COPYING": "COPYING.gzip",
        "usr/kinit/README": "README.kinit"}

configh = """
#ifndef _LINUX_CONFIG_H
#define _LINUX_CONFIG_H

#include <linux/autoconf.h>

#endif
"""

#~ shelltools.export("C_INCLUDE_PATH", "/usr/include")

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    # we must include headers, but kernel headers chango too fast, maybe we should
    # go back to adding them as a patch
    # shelltools.sym("/lib/modules/%s/build" % KDIR, "linux")
    #~ shelltools.copytree("/lib/modules/%s/build" % KDIR, "linux")

    shelltools.makedirs("linux/include")
    shelltools.system("ln -s /usr/include/linux linux/include/")
    shelltools.system("ln -s /usr/include/asm linux/include/")
    shelltools.system("ln -s /usr/include/asm-generic linux/include/")
    # don't install kernel headers
    pisitools.dosed("scripts/Kbuild.install", ".*headers_install")

    # set the build directory
    #~ shelltools.echo("MCONFIG", "KRNLOBJ = /lib/modules/%s/build" % KDIR)
    #shelltools.sym("../linux-3.7","linux")

    # Workaround for prelink warnings
    shelltools.echo("70klibc", 'PRELINK_PATH_MASK="/usr/lib/klibc"')

    pisitools.dosed("Makefile", "/man", "/share/man")

#    shelltools.echo("linux/include/linux/config.h", configh)

def build():
    shelltools.export("ARCH", "")
    autotools.make('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                    EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                    HOSTCC="%s" CC="%s" \
                    KLIBCARCH=%s \
                    KLIBCASMARCH=x86 \
                    libdir=/usr/lib \
                    SHLIBDIR=/lib \
                    mandir=/usr/share/man \
                    INSTALLDIR=/usr/lib/klibc' % (get.CC(), get.CC(), klibcarch))

def install():
    shelltools.export("ARCH", "")
    autotools.rawInstall('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                          EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                          HOSTCC="%s" CC="%s" \
                          KLIBCARCH=%s \
                          KLIBCASMARCH=x86 \
                          libdir=/usr/lib \
                          SHLIBDIR=/lib \
                          mandir=/usr/share/man \
                          INSTALLROOT="%s" \
                          INSTALLDIR=/usr/lib/klibc' % (get.CC(), get.CC(), klibcarch, get.installDIR()))

    asmSrcDir = "linux/arch/x86/include/asm"
    asmTargetDir = "/usr/lib/klibc/include/asm"

    # FIXME: we probably don't need old kernel workarounds anymore
    # just a workaround for installer bug with 2.6.24, will make it sane later
    #pisitools.remove(asmTargetDir)
    #pisitools.dosym("asm-x86", asmTargetDir)

    # yet another new kernel compatibility workaround for 2.6.28 and above
    #for f in shelltools.ls(asmSrcDir):
    #    pisitools.insinto(asmTargetDir, "%s/%s" % (asmSrcDir, f))

    fixperms("%s/usr/lib/klibc/include" % get.installDIR())

    for f in ["gunzip", "zcat"]:
        pisitools.remove("/usr/lib/klibc/bin/%s" % f)
        pisitools.dosym("gzip", "/usr/lib/klibc/bin/%s" % f)

    pisitools.dodoc("README", "usr/klibc/LICENSE", "usr/klibc/CAVEATS")

    for f in docs:
        pisitools.newdoc(f, docs[f])

    pisitools.insinto("/usr/lib/klibc/include/linux", "linux/include/linux/*")
    pisitools.insinto("/usr/lib/klibc/include/asm", "linux/include/asm/*")
    pisitools.insinto("/usr/lib/klibc/include/asm-generic", "linux/include/asm-generic/*")
