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
    
    autotools.configure("--with-libwrap \
                         --with-loadavg \
                         --with-inet6 \
                         --with-labeled-networking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-contrib")
    
    pisitools.dodoc("CHANGELOG", "COPYRIGHT", "README", "TODO")