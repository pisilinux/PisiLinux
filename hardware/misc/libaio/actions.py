#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("src/Makefile", "=-shared", r"= -Wl,-O1,--as-needed -shared")
    if get.buildTYPE() == "emul32":
        pisitools.dosed(".", "\/lib$", r"/lib%s\n" % "32" if get.buildTYPE() == "emul32" else "", filePattern="Makefile")
    autotools.make()

#def check():
    #shelltools.cd("harness")
    #pisitools.dodir("testdir")

    #autotools.make("check prefix=../src libdir=../src")


def install():

    if get.buildTYPE() == "emul32":
        autotools.rawInstall("prefix=%s/usr \
                              includedir=%s/usr/include \
                              libdir%s/=usr/lib32 " % ((get.installDIR(), ) * 3))
        pisitools.remove("/usr/lib32/libaio.a")
    else:
        autotools.rawInstall("prefix=%s/usr \
                              includedir=%s/usr/include \
                              libdir%s/=usr/lib " % ((get.installDIR(), ) * 3))
        pisitools.remove("/usr/lib/libaio.a")

        pisitools.dodoc("ChangeLog", "COPYING", "TODO")
