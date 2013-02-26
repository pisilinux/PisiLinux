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

WorkDir = "%s-opensource-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--localstatedir=/var \
                         --enable-shared \
                         --disable-static \
                         --without-internal-zlib \
                         --with-debug \
                         --with-iodbc \
                         --disable-demo-vad \
                         --disable-hslookup \
                         --enable-openssl \
                         --enable-xml")

def build():
    #tests fail with parallel build
    autotools.make("-j1")

"""
def check():
    #to fix thook.sh test this is required
    shelltools.export("HOST", "localhost")

    autotools.make("-j1 check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")

    #Rename generic filenames
    for f in ("inifile" ,"isql", "isqlw", "isql-iodbc", "isqlw-iodbc"):
        pisitools.domove("/usr/bin/%s" % f, "/usr/bin/", "virtuoso-%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "LICENSE", "NEWS", "README*")

    #remove duplicate documents
    pisitools.removeDir("/usr/share/virtuoso/doc")

    pisitools.dodir("/etc/virtuoso")
    pisitools.domove("/var/lib/virtuoso/db/virtuoso.ini", "/etc/virtuoso")
