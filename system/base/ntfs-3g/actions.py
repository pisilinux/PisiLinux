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

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --with-fuse=external \
                         --enable-extras \
                         --enable-posix-acls \
                         --enable-ldscript \
                         --disable-ldconfig")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/bin/ntfs-3g.*", "/bin")

    # Create some compat symlinks
    pisitools.dosym("/bin/ntfs-3g", "/sbin/mount.ntfs")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "CREDITS", "NEWS", "README")
    pisitools.dosym("/usr/share/doc/ntfs-3g", "/usr/share/doc/ntfsprogs")
