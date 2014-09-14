#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    # Filter out -nostdlib from libtool
    shelltools.copy("/usr/bin/libtool", "src")
    pisitools.dosed("src/libtool", "-nostdlib ", "")

    for i in ["src/def_makefile", "src/makefile", "src/mfile"]:
             pisitools.dosed(i, "--mode=compile", "--tag=CC --mode=compile")
             
    for i in ["src/def_makefile", "src/makefile", "src/mfile"]:
             pisitools.dosed(i, "--mode=link", "--tag=LD --mode=link")        
             
    shelltools.cd("src")
    autotools.rawConfigure("DEF_PREFIX=/usr SHARED=on NTL_GF2X_LIB=on NTL_GMP_LIP=on")

def build():
    autotools.make("-C src -j1")

def check():
    autotools.make("-C src -k check -j1")

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s \
                          DOCDIR=/usr/share/doc/%s \
                          INCLUDEDIR=/usr/include \
                          LIBDIR=/usr/lib" % (get.installDIR(), get.srcNAME()))

    pisitools.dodoc("../README")