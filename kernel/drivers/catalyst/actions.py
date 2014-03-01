#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

arch = get.ARCH().replace("i686", "x86")
version = get.srcVERSION()
driver = "catalyst"
libdir = "/usr/lib/%s" % driver
datadir = "/usr/share/%s" % driver

def setup():
    shelltools.system("sh amd-catalyst-%s-linux-x86.%s.run --extract archive_files" % (version, arch))
    shelltools.move("archive_files/*", ".")
    shelltools.system("sh ./ati_make.sh")
    
    shelltools.system("patch -p1  < arch_3.13_kernel_acpi_node.patch")
    shelltools.system("patch -p1  < lano1106_fglrx-13.8_proc.patch")
    shelltools.system("patch -p1  < lano1106_fglrx_intel_iommu.patch")
    shelltools.system("patch -p1  < lano1106_kcl_agp_13_4.patch")
    shelltools.system("patch -p1  < looks_like_amd_forgot_this.patch")
    shelltools.system("patch -p1  < makefile_compat.patch")
    
    shelltools.cd("common/lib/modules/fglrx/build_mod")
    shelltools.system("2.6.x/Makefile")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())