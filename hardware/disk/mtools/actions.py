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
    #for i in ["mtools.texi"]:
    #    pisitools.dosed(i, "/usr/local/etc", "/etc")

    shelltools.export("INSTALL_PROGRAM", "install")
    autotools.autoreconf("-fi")
    autotools.configure("--sysconfdir=/etc/mtools \
                         --includedir=/usr/src/linux/include \
                         --without-x \
                         --disable-floppyd")

def build():
    autotools.make()

def install():
    # autotools.install("sysconfdir=%s/etc/mtools" % get.installDIR())
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/etc/mtools","mtools.conf")

    pisitools.dodoc("COPYING", "README*", "Release.notes")
