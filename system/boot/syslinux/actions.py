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

tools = ["sha1pass", "md5pass", "mkdiskimage", "keytab-lilo", "syslinux2ansi", "lss16toppm","pxelinux-options"]
datadir = "/usr/lib/syslinux"

NoStrip = ["/sbin", "/usr/lib"]

def setup():
    # previously linked to probably some other glibc, better force recompile
    # shelltools.unlink("gethostip")
    # shelltools.chmod("add_crc", 0755)
    pass

def build():
    # shelltools.export("CFLAGS", "-Werror -Wno-unused -finline-limit=2000")
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("LDFLAGS", "")

    autotools.make('DATE="PARDUS" spotless')
    autotools.make('DATE="PARDUS"')
    # autotools.make('DATE="PARDUS" installer')
    # autotools.make('DATE="PARDUS" -C sample tidy')

def install():
    autotools.rawInstall('INSTALLROOT=%s MANDIR="/usr/share/man" AUXDIR="/usr/lib/syslinux"' % get.installDIR())
    for f in tools:
        pisitools.insinto(datadir, "utils/"+f)

    pisitools.dodoc("README", "NEWS", "doc/*.txt", "doc/logo/LICENSE")
    pisitools.remove("/usr/bin/gethostip")
