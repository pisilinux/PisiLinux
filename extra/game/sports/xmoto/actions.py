#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-rpath \
                         --with-internal-xdg=1 \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.insinto("/usr/share/applications", "extra/xmoto.desktop")
    pisitools.insinto("/usr/share/pixmaps", "extra/xmoto.xpm")
