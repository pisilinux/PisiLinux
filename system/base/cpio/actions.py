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
    #who knows pisitools.dosed :)
    cmd="sed -i '/gets is a security hole/d' gnu/stdio.in.h"
    shelltools.system(cmd)
    autotools.configure("--enable-nls \
                         --bindir=/bin \
                         --with-rmt=/usr/sbin/rmt \
                         --disable-rpath")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/man/man1/mt.1")
    pisitools.removeDir("/usr/libexec")

    pisitools.dodoc("ChangeLog", "NEWS", "README")

