#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xz-%s" % get.srcVERSION()

def setup():
    options = " --disable-static \
                --disable-rpath"

    if get.buildTYPE() == "emul32":
        # Suggested C(XX)FLAGS by the upstream author
        shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=32 -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -D_FILE_OFFSET_BITS=32" % get.CXXFLAGS())
    else:
        shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CXXFLAGS())

    autotools.configure(options)

    # Fix overlinking
    pisitools.dosed("libtool", "-pthread", "-lpthread")
    pisitools.dosed("src/liblzma/liblzma.pc.in", "@PTHREAD_CFLAGS@", "")

    # Remove RPATH
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def check():
    shelltools.export("LD_LIBRARY_PATH", "%s/src/liblzma/.libs" % get.curDIR())
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if not get.buildTYPE() == "emul32":
        pisitools.remove("/usr/share/man/man1/lzmadec.1")
        pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")