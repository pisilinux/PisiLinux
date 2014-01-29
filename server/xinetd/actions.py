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
    shelltools.system("sed -i -e '/^LIBS/s/-lpset/& -ltirpc/' xinetd/Makefile.in")
    shelltools.system("sed -i -e '/register unsigned count/s/register//' xinetd/itox.c")
    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/bin \
                         --without-libwrap \
                         --with-loadavg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/bin/", "xinetd/xinetd")
    pisitools.insinto("/usr/sbin/", "xinetd/xinetd")
    pisitools.dodoc("TODO", "README", "COPYRIGHT", "CHANGELOG")
