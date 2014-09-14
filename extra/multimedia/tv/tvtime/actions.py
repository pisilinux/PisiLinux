#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


flags = "%s -fPIC" % get.CFLAGS() if get.ARCH() == "x86_64" else get.CFLAGS()

def setup():
    # shelltools.export("CFLAGS", flags)
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-nls \
                         --with-xinerama")

def build():
    autotools.make()
    shelltools.cd("po")
    autotools.make("update-po")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # We will use our desktop file
    pisitools.remove("/usr/share/applications/net-tvtime.desktop")

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")
