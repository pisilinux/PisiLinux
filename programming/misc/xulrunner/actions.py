#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

import os

WorkDir = "mozilla-release"
NoStrip = ["/usr/include", "/usr/share/idl"]
XulVersion = "29.0"
XulDir = "/usr/lib/%s-%s" % (get.srcNAME(), XulVersion)
ObjDir = "obj-%s-unknown-linux-gnu" % get.ARCH() if get.ARCH() == "x86_64" else "obj-%s-pc-linux-gnu" % get.ARCH()

def setup():
    pisitools.ldflags.add("-Wl,-rpath,/usr/lib/xulrunner-%s" % XulVersion)
    # Write xulrunner version correctly including the minor part
    for f in ("xulrunner/installer/Makefile.in", ".mozconfig", "20-xulrunner.conf"):
        pisitools.dosed(f, "PSPEC_VERSION", XulVersion)

    # Mozilla sticks on with autoconf-213, so use autoconf-213 which we provide via a hacky patch to produce configure
    shelltools.chmod("autoconf-213/autoconf-2.13", 0755)

    # Set job count for make
    pisitools.dosed(".mozconfig", "%%JOBS%%", get.makeJOBS())

    shelltools.system("/bin/bash ./autoconf-213/autoconf-2.13 --macro-dir=autoconf-213/m4")
    shelltools.cd("js/src")
    shelltools.system("/bin/bash ../../autoconf-213/autoconf-2.13 --macro-dir=../../autoconf-213/m4")
    shelltools.cd("../..")
    # configure script misdetects the preprocessor without an optimization level
    # https://bugs.archlinux.org/task/34644
    shelltools.system("sed -i '/ac_cpp=/s/$CPPFLAGS/& -O2/' configure")
    shelltools.makedirs(ObjDir)

def build():
    shelltools.cd(ObjDir)
    autotools.make("-f ../client.mk build")

def install():
    autotools.rawInstall("-f client.mk DESTDIR=%s" % get.installDIR())

    executable = ["xpcshell", "xpidl", "xpt_dump", "xpt_link",\
                  "xulrunner-stub", "mozilla-xremote-client"]

    for exe in executable:
        pisitools.dosym("%s/%s" % (XulDir, exe), "/usr/bin/%s" % exe)

    pisitools.dodir("%s/dictionaries" % XulDir)
    shelltools.touch("%s%s/dictionaries/tr-TR.aff" % (get.installDIR(), XulDir))
    shelltools.touch("%s%s/dictionaries/tr-TR.dic" % (get.installDIR(), XulDir))

    shelltools.chmod("%s/usr/lib/xulrunner-devel-29.0/sdk/bin/xpt.py" % get.installDIR(), 0755)
    shelltools.chmod("%s/usr/lib/xulrunner-devel-29.0/sdk/bin/xpcshell" % get.installDIR(), 0755)
    # Remove unnecessary executable bits
    for d in ("%s/usr/share" % get.installDIR(), "%s/usr/include" % get.installDIR()):
        for root, dirs, files in os.walk(d):
            for file in files:
                shelltools.chmod(os.path.join(root, file), 0644)

    pisitools.insinto("/etc/ld.so.conf.d", "20-xulrunner.conf", "xulrunner.conf")
