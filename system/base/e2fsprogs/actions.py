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

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.rawConfigure("--enable-elf-shlibs \
                            --disable-e2initrd-helper \
                            --disable-libblkid \
                            --disable-libuuid \
                            --disable-fsck \
                            --disable-uuidd \
                            --enable-symlink-install \
                            --without-included-gettext")

def build():
    autotools.make()

def check():
    # remove sandbox violating test
    for d in ("f_ext_journal", "t_ext_jnl_rm"):
        shelltools.unlinkDir("%s/e2fsprogs-%s/tests/%s/" % (get.workDIR(), get.srcVERSION(), d))
    autotools.make("check")

def install():
    autotools.rawInstall("install install-libs LDCONFIG=/bin/true \
                          DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % get.installDIR())

    # Unneeded stuff
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("COPYING", "README", "RELEASE-NOTES")
