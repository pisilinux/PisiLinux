#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fPIC -D_GNU_SOURCE")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-nls \
                         --disable-audit \
                         --enable-securedir=/lib/security \
                         --enable-isadir=/lib/security")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    # Update .po files
    autotools.make("-C po update-gmo")

    autotools.make()

def check():
    autotools.make("check")

    # dlopen check
    shelltools.system("./dlopen-test.sh")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/Linux-PAM/")

    pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
