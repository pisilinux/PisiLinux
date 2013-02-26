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


def setup():
    autotools.autoreconf("-vfi")

    # Remove -Wall from default flags. The makefiles enable enough warnings
    # themselves, and they use -Werror.
    shelltools.export("CFLAGS", get.CFLAGS().replace("-Wall", ""))

    autotools.configure("--program-prefix=\"eu-\" \
                         --enable-thread-safety \
                         --disable-nls \
                         --with-zlib \
                         --with-bzlib")
                         # --with-lzma \

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Don't remove all the static libs as libebl.a is needed by other packages
    pisitools.remove("/usr/lib/libelf.a")
    pisitools.remove("/usr/lib/libasm.a")
    pisitools.remove("/usr/lib/libdw.a")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "NOTES", "README", "THANKS", "TODO")
