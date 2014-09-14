#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

tools = ["sha1pass", "md5pass", "mkdiskimage", "keytab-lilo", "syslinux2ansi", "lss16toppm","pxelinux-options"]
datadir = "/usr/lib/syslinux"

NoStrip = ["/sbin", "/usr/lib"]

pisitools.flags.remove("-fPIC")

def build():
    # shelltools.export("CFLAGS", "-Werror -Wno-unused -finline-limit=2000")
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("LDFLAGS", "")

    autotools.make('DATE="PisiLinux" spotless')
    autotools.make('DATE="PisiLinux"')
    # autotools.make('DATE="PARDUS" installer')
    # autotools.make('DATE="PARDUS" -C sample tidy')

def install():
    autotools.rawInstall('INSTALLROOT=%s MANDIR="/usr/share/man" AUXDIR="/usr/lib/syslinux"' % get.installDIR())
    for f in tools:
        pisitools.insinto(datadir, "utils/"+f)

    #pisitools.domove("/usr/lib/syslinux/libutil_com.c32","/usr/lib/syslinux/com32/libutil")
    #pisitools.domove("/usr/lib/syslinux/libcom32.c32","/usr/lib/syslinux/com32/lib")
    pisitools.dodoc("README", "NEWS", "doc/*.txt", "doc/logo/LICENSE")
    pisitools.remove("/usr/bin/gethostip")
