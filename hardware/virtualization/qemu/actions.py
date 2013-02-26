#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/usr/share/qemu"]

shelltools.export("LC_ALL", "C")

# disable debug to prevent memory exhaustion by linker
# cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "").replace("-ggdb3 -funwind-tables -fasynchronous-unwind-tables", "")
cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "")

#extraldflags="-Wl,--build-id"
#buildldflags="VL_LDFLAGS=-Wl,--build-id"
extraldflags=""
buildldflags=""

soundDrivers = "pa,sdl,alsa,oss"
builddirkvmtest = "kvm/test"

#targetKvmList = "i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user"
targetListKvm = "x86_64-softmmu"
targetList = "i386-softmmu x86_64-softmmu arm-softmmu cris-softmmu m68k-softmmu \
              mips-softmmu mipsel-softmmu mips64-softmmu mips64el-softmmu ppc-softmmu \
              ppcemb-softmmu ppc64-softmmu sh4-softmmu sh4eb-softmmu sparc-softmmu \
              i386-linux-user x86_64-linux-user alpha-linux-user arm-linux-user \
              armeb-linux-user cris-linux-user m68k-linux-user mips-linux-user \
              mipsel-linux-user ppc-linux-user ppc64-linux-user ppc64abi32-linux-user \
              sh4-linux-user sh4eb-linux-user sparc-linux-user sparc64-linux-user \
              sparc32plus-linux-user"


cfgParamsCommon = '--prefix=/usr \
                  --sysconfdir=/etc \
                  --mandir=/usr/share/man \
                  --cc="%s" \
                  --host-cc="%s" \
                  --extra-cflags="%s" \
                  --extra-ldflags="%s" \
                  --audio-drv-list="%s" \
                  --disable-xen \
                  --disable-werror \
                  --disable-strip' % (get.CC(), get.CC(), cflags, extraldflags, soundDrivers)


def printfancy(msg):
    print
    print "===== %s =====" % msg
    print

def setup():
    # disable fdt until dtc is in repo
    # pisitools.dosed("configure", 'fdt="yes"', 'fdt="no"')

    shelltools.export("CFLAGS", cflags)
    shelltools.export("LDFLAGS", extraldflags)

    # different build dir setups are not supported yet, so we build kvm by hand for now
    printfancy("configuring kvm")
    autotools.rawConfigure('%s \
                            --target-list="%s" \
                            ' % (cfgParamsCommon, targetListKvm))

    printfancy("building kvm")
    autotools.make("V=1 -j1 config-host.h %s" % buildldflags)
    autotools.make("V=1 %s" % buildldflags)
    shelltools.copy("x86_64-softmmu/qemu-system-x86_64", "qemu-kvm")
    autotools.make("clean")


    # kvmtest stuff is not in upstream tarball anymore, but they may put it back, be ready
    #printfancy("configuring kvmtest")
    #shelltools.cd(builddirkvmtest)
    #autotools.rawConfigure("--prefix=/usr \
    #                        --kerneldir=../../kernel")
    #shelltools.cd("../..")


    printfancy("configuring qemu")
    autotools.rawConfigure('%s \
                            --target-list="%s" \
                            --disable-kvm \
                            ' % (cfgParamsCommon, targetList))
                            #--interp-prefix=%{_prefix}/qemu-%%M \

                            #--enable-system \
                            #--enable-linux-user \


def build():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("LDFLAGS", extraldflags)

    printfancy("building qemu")
    autotools.make("V=1 -j1 config-host.h %s" % buildldflags)
    autotools.make("V=1 %s" % buildldflags)

    #printfancy("building kvmtest")
    #autotools.make("-C %s V=1 kvmtrace" % builddirkvmtest)

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # Install kvm-tools
    #pisitools.dobin("kvm/test/kvmtrace")
    #pisitools.dobin("kvm/test/kvmtrace_format")
    #pisitools.dobin("kvm/kvm_stat")
    pisitools.dobin("qemu-kvm")

    pisitools.insinto("/etc/sasl2/", "qemu.sasl", "qemu.conf")

    for i in ["pc-bios/README", "LICENSE", "TODO", "README", "COPYING*", "qemu-doc.html", "qemu-tech.html"]:
        pisitools.dodoc(i)

