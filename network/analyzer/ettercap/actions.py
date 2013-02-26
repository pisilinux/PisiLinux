#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ettercap"
KeepSpecial = ["libtool"]

def setup():
    shelltools.export("CFLAGS", "%s -DLTDL_SHLIB_EXT='\".so\"'" % get.CFLAGS())
    autotools.configure("--with-openssl=/usr \
                         --with-ncurses \
                         --enable-gtk \
                         --without-included-ltdl \
                         --disable-ltdl-install \
                         --enable-plugins")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/pixmaps")
    pisitools.dosym("/usr/share/ettercap/ettercap.png", "/usr/share/pixmaps/ettercap.png")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README*", "LICENSE")
