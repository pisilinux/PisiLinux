#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Togl%s" % get.srcVERSION()

extra_params = "--enable-64bit" if get.ARCH()=="x86_64" else ""

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-threads \
                         --enable-shared %s" % extra_params)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove empty dir.
    pisitools.removeDir("/usr/bin")

    pisitools.remove("/usr/lib/libToglstub2.0.a")

    pisitools.domove("/usr/lib/Togl2.0/LICENSE", "%s/%s" %(get.docDIR(), get.srcNAME()))

    pisitools.dohtml("doc/*")
    pisitools.dodoc("README*")
