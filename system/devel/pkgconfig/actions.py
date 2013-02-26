#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pkg-config-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-installed-popt \
                         --with-pc-path=/usr/lib/pkgconfig:/usr/share/pkgconfig")

def check():
    autotools.make("check")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/lib/pkgconfig")
    pisitools.dodir("/usr/share/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
