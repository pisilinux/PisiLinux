#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    if get.buildTYPE() == "emul32":
        pisitools.dosed("config/Makefile.linux", "LD = cc", "LD = gcc -m32")
        autotools.make('CC="%s -m32" CXXFLAGS="%s"' % (get.CC(), get.CXXFLAGS()))
        return
    else:
        autotools.make('CC=%s CXXFLAGS="%s"' % (get.CC(), get.CXXFLAGS()))
        return

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("GLEW_DEST=%s/usr/ \
                              INCDIR=%s/emul32 \
                              BINDIR=%s/emul32 \
                              LIBDIR=%s//usr/lib32" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR()))

        pisitools.remove("/usr/lib32/libGLEW.a")
        return

    autotools.rawInstall("GLEW_DEST=%s/usr/ \
                          INCDIR=%s/usr/include/GL \
                          BINDIR=%s/usr/bin/ \
                          LIBDIR=%s//usr/lib" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.remove("/usr/lib/libGLEW.a")
    pisitools.dohtml("doc/*")
    pisitools.dodoc("README.txt", "doc/*.txt")
