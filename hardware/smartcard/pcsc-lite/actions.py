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

#USBDROPDIR   = "/usr/lib%s/pcsc/drivers" % ("32" if \
#        get.buildTYPE() == "emul32" else "")

USBDROPDIR = "/usr/lib/pcsc/drivers"

def setup():
    options = "--enable-usbdropdir=%s \
               --disable-dependency-tracking \
               --disable-static" % USBDROPDIR

    """
    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
    """

    autotools.autoreconf("-fi")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir(USBDROPDIR)

    """
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        return
    """

    pisitools.dodir("/etc/reader.conf.d")

    pisitools.dodoc("AUTHORS", "ChangeLog", "DRIVERS", "HELP", "NEWS",
                    "README", "SECURITY", "doc/README.DAEMON")
