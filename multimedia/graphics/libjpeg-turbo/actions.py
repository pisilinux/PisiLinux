#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    if not get.buildTYPE() == "emul32":
        autotools.configure("--with-jpeg8")
    else:
        pisitools.dosed("configure", "(NAFLAGS='-fel)f64( -DELF -D__x86_64__)", "\\1f32\\2")
        autotools.configure("--with-jpeg8 --without-simd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    # provide jpegint.h as it is required by various software
    pisitools.insinto("/usr/lib/include", "jpegint.h")
