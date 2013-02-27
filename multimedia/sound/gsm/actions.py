#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="gsm-1.0-pl13"

def setup():
    multilib = " -m32" if get.buildTYPE() == "emul32" else ""
    pisitools.dosed("Makefile", "pardusCC", "%s %s" % (get.CC(), multilib))
    pisitools.dosed("Makefile", "pardusCFLAGS", "%s %s" % (get.CFLAGS(), multilib))

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s bindir=/emul32 libdir=/usr/lib32" % get.installDIR())
        pisitools.remove("/usr/lib32/libgsm.a")
        return
    else:
        autotools.rawInstall("DESTDIR=%s bindir=/usr/bin" % get.installDIR())

    for bin in ["tcat","untoast"]:
        pisitools.remove("/usr/bin/%s" % bin)
        pisitools.dosym("toast", "/usr/bin/%s" % bin)

    # Move gsm.h out of gsm subdir
    # pisitools.insinto("/usr/include","inc/gsm.h")
    # pisitools.removeDir("/usr/include/gsm")

    # No static libs
    pisitools.remove("/usr/lib/libgsm.a")

    pisitools.dodoc("ChangeLog", "COPYRIGHT", "MACHINES", "MANIFEST", "README")
