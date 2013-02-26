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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -D_GNU_SOURCE" % get.CFLAGS())

    libtools.libtoolize("-f")
    autotools.autoreconf("-fi")
    autotools.rawConfigure("--disable-prelude \
                            --disable-dependency-tracking \
                            --enable-audit=no \
                            --enable-db=no \
                            --enable-nls \
                            --enable-securedir=/lib/security \
                            --enable-isadir=/lib/security")

def build():
    # Update .po files
    autotools.make("-C po update-gmo")

    autotools.make()

def check():
    autotools.make("check")
    #One test failed now, fix it

    # dlopen check
    shelltools.system("./dlopen-test.sh")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: Check whether /var is empty!
    #~ pisitools.removeDir("/var")

    pisitools.removeDir("/usr/share/doc/Linux-PAM/")

    pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
