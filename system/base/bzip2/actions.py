#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

libversion = get.srcVERSION()

def build():
    autotools.make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC"' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    autotools.make('CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" -f Makefile-libbz2_so' % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    # No static libs
    pisitools.removeDir("/usr/lib")
    pisitools.domove("/usr/bin/", "/")

    for link in ("/bin/bunzip2", "/bin/bzcat"):
        pisitools.remove(link)
        pisitools.dosym("/bin/bzip2", link)

    pisitools.dolib("libbz2.so.%s" % libversion, "/lib")

    pisitools.dosym("libbz2.so.1", "/lib/libbz2.so")
    pisitools.dosym("libbz2.so.%s" % libversion, "/lib/libbz2.so.1")

    pisitools.dohtml("manual.html")
    pisitools.dodoc("README", "CHANGES", "bzip2.txt")
