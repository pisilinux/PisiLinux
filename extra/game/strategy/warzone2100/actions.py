#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

mandir = "/usr/share/man"

def setup():
    autotools.configure('--with-icondir=/usr/share/pixmaps \
                         --disable-rpath \
                         --with-backend=qt \
                         --with-distributor="PisiLinux" \
                         --disable-debug')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if shelltools.isDirectory("%s/%s" % (get.installDIR(), mandir)):
        pisitools.removeDir(mandir)

